import os
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# --- Constants ---
EXPERIMENTS_DIR = "research/2024-07-25-knowledge-graph-gbt-movie-ratings/experiments"
DATA_FILE = "movielens_100k.csv"
TOPO_FEATURES_FILE = "topological_features.csv"
EMBEDDINGS_FILE = "node_embeddings.csv"

# --- Main Function ---

def run_experiment():
    """
    Trains and evaluates a baseline and an augmented XGBoost model to compare
    the impact of graph-derived features on rating prediction.
    """
    # --- 1. Load Data ---
    print("Loading data...")
    try:
        df = pd.read_csv(os.path.join(EXPERIMENTS_DIR, DATA_FILE))
        topo_features = pd.read_csv(os.path.join(EXPERIMENTS_DIR, TOPO_FEATURES_FILE))
        embeddings = pd.read_csv(os.path.join(EXPERIMENTS_DIR, EMBEDDINGS_FILE))
    except FileNotFoundError as e:
        print(f"Error: A required data file was not found: {e}")
        print("Please ensure scripts 01, 02, and 03 have been run successfully.")
        return

    # --- 2. Prepare Features ---
    print("Preparing features...")

    # Merge topological features for users and movies
    user_topo = topo_features[topo_features['node_id'].str.startswith('user_')].rename(
        columns={'node_id': 'user_node_id', 'degree_centrality': 'user_degree', 'pagerank': 'user_pagerank'})
    movie_topo = topo_features[topo_features['node_id'].str.startswith('movie_')].rename(
        columns={'node_id': 'movie_node_id', 'degree_centrality': 'movie_degree', 'pagerank': 'movie_pagerank'})

    # Merge embeddings for users and movies
    user_emb = embeddings[embeddings['node_id'].str.startswith('user_')].add_prefix('user_')
    movie_emb = embeddings[embeddings['node_id'].str.startswith('movie_')].add_prefix('movie_')

    # Create string node IDs in the main dataframe for merging
    df['user_node_id'] = 'user_' + df['user_id'].astype(str)
    df['movie_node_id'] = 'movie_' + df['movie_id'].astype(str)

    # Merge all features into the main dataframe
    merged_df = df.merge(user_topo, on='user_node_id', how='left')
    merged_df = merged_df.merge(movie_topo, on='movie_node_id', how='left')
    merged_df = merged_df.merge(user_emb, left_on='user_node_id', right_on='user_node_id', how='left')
    merged_df = merged_df.merge(movie_emb, left_on='movie_node_id', right_on='movie_node_id', how='left')

    # Fill any NaNs that might result from merges (e.g., nodes not in graph)
    merged_df.fillna(0, inplace=True)

    # Define feature sets
    baseline_features = ['user_id', 'movie_id']

    augmented_features = baseline_features + [
        'user_degree', 'user_pagerank', 'movie_degree', 'movie_pagerank'
    ] + [col for col in merged_df.columns if 'user_emb_' in col or 'movie_emb_' in col]

    target = 'rating'

    X = merged_df
    y = merged_df[target]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # --- 3. Train and Evaluate Baseline Model ---
    print("Training and evaluating baseline XGBoost model...")

    X_train_base = X_train[baseline_features]
    X_test_base = X_test[baseline_features]

    xgb_base = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42)
    xgb_base.fit(X_train_base, y_train)

    preds_base = xgb_base.predict(X_test_base)
    rmse_base = np.sqrt(mean_squared_error(y_test, preds_base))

    # --- 4. Train and Evaluate Augmented Model ---
    print("Training and evaluating augmented XGBoost model...")

    X_train_aug = X_train[augmented_features]
    X_test_aug = X_test[augmented_features]

    xgb_aug = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42)
    xgb_aug.fit(X_train_aug, y_train)

    preds_aug = xgb_aug.predict(X_test_aug)
    rmse_aug = np.sqrt(mean_squared_error(y_test, preds_aug))

    # --- 5. Compare Results ---
    print("\n--- Experiment Results ---")
    print(f"Baseline Model RMSE: {rmse_base:.4f}")
    print(f"Augmented Model RMSE: {rmse_aug:.4f}")

    improvement = ((rmse_base - rmse_aug) / rmse_base) * 100
    if improvement > 0:
        print(f"The augmented model showed an improvement of {improvement:.2f}% over the baseline.")
    else:
        print("The augmented model did not show an improvement over the baseline.")

# --- Main Execution ---

if __name__ == "__main__":
    run_experiment()
