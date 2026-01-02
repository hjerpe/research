import os
import pandas as pd
import networkx as nx
import pickle

# --- Constants ---
INPUT_FILE = "movielens_100k.csv"
OUTPUT_GRAPH_FILE = "movielens_kg.gpickle"
OUTPUT_FEATURES_FILE = "topological_features.csv"
EXPERIMENTS_DIR = "research/2024-07-25-knowledge-graph-gbt-movie-ratings/experiments"

# --- Main Function ---

def build_graph_and_extract_features():
    """
    Builds a knowledge graph from the MovieLens dataset, calculates topological
    features, and saves the graph and features to disk.
    """
    input_path = os.path.join(EXPERIMENTS_DIR, INPUT_FILE)

    print(f"Loading data from {input_path}...")
    try:
        df = pd.read_csv(input_path)
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_path}")
        print("Please run the '01_prepare_data.py' script first.")
        return

    print("Building the knowledge graph...")
    G = nx.Graph()

    # Get all genre columns
    genre_cols = ['action', 'adventure', 'animation', 'childrens', 'comedy', 'crime',
                  'documentary', 'drama', 'fantasy', 'film_noir', 'horror', 'musical',
                  'mystery', 'romance', 'sci_fi', 'thriller', 'war', 'western']

    for _, row in df.iterrows():
        user_id = f"user_{row['user_id']}"
        movie_id = f"movie_{row['movie_id']}"
        rating = row['rating']

        # Add nodes with type attribute
        G.add_node(user_id, type='user')
        G.add_node(movie_id, type='movie', title=row['movie_title'])

        # Add edge between user and movie with rating as an attribute
        G.add_edge(user_id, movie_id, rating=rating)

        # Add genre nodes and edges from movie to genre
        for genre in genre_cols:
            if row[genre] == 1:
                genre_id = f"genre_{genre}"
                G.add_node(genre_id, type='genre')
                G.add_edge(movie_id, genre_id)

    print(f"Graph built with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

    print("Calculating topological features...")
    # Calculate degree centrality and PageRank
    degree_centrality = nx.degree_centrality(G)
    pagerank = nx.pagerank(G, alpha=0.85)

    # Combine features into a DataFrame
    features_df = pd.DataFrame({
        'node_id': list(degree_centrality.keys()),
        'degree_centrality': list(degree_centrality.values()),
        'pagerank': list(pagerank.values())
    })

    print("Saving graph and features...")
    # Save the graph object
    graph_output_path = os.path.join(EXPERIMENTS_DIR, OUTPUT_GRAPH_FILE)
    with open(graph_output_path, 'wb') as f:
        pickle.dump(G, f, pickle.HIGHEST_PROTOCOL)
    print(f"Graph saved to {graph_output_path}")

    # Save the features
    features_output_path = os.path.join(EXPERIMENTS_DIR, OUTPUT_FEATURES_FILE)
    features_df.to_csv(features_output_path, index=False)
    print(f"Features saved to {features_output_path}")

# --- Main Execution ---

if __name__ == "__main__":
    build_graph_and_extract_features()
