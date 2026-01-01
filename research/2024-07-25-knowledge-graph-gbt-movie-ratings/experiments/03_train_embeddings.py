import os
import pandas as pd
import torch
from pykeen.pipeline import pipeline
from pykeen.triples import TriplesFactory

# --- Constants ---
INPUT_FILE = "movielens_100k.csv"
OUTPUT_EMBEDDINGS_FILE = "node_embeddings.csv"
EXPERIMENTS_DIR = "research/2024-07-25-knowledge-graph-gbt-movie-ratings/experiments"

# Model Hyperparameters
EMBEDDING_DIM = 64
NUM_EPOCHS = 10  # A small number for a quick experiment
BATCH_SIZE = 128

# --- Main Function ---

def train_and_save_embeddings():
    """
    Trains knowledge graph embeddings using PyKEEN and saves them to a file.
    """
    input_path = os.path.join(EXPERIMENTS_DIR, INPUT_FILE)

    print(f"Loading data from {input_path}...")
    try:
        df = pd.read_csv(input_path)
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_path}")
        print("Please run '01_prepare_data.py' script first.")
        return

    print("Creating triples for PyKEEN...")
    triples = []

    # Get all genre columns
    genre_cols = ['action', 'adventure', 'animation', 'childrens', 'comedy', 'crime',
                  'documentary', 'drama', 'fantasy', 'film_noir', 'horror', 'musical',
                  'mystery', 'romance', 'sci_fi', 'thriller', 'war', 'western']

    # Create user-movie interaction triples
    for _, row in df.iterrows():
        user_id = f"user_{row['user_id']}"
        movie_id = f"movie_{row['movie_id']}"

        # Relation: user -> rated -> movie
        triples.append([user_id, 'rated', movie_id])

        # Relation: movie -> has_genre -> genre
        for genre in genre_cols:
            if row[genre] == 1:
                genre_id = f"genre_{genre}"
                triples.append([movie_id, 'has_genre', genre_id])

    triples_df = pd.DataFrame(triples, columns=['head', 'relation', 'tail'])

    # Create a TriplesFactory from the labeled triples
    tf = TriplesFactory.from_labeled_triples(triples_df.to_numpy())

    # Split into training and testing
    training_factory, testing_factory = tf.split([0.8, 0.2], random_state=42)

    print("Starting PyKEEN pipeline to train embeddings...")
    pipeline_result = pipeline(
        training=training_factory,
        testing=testing_factory,
        model='TransE',
        model_kwargs=dict(embedding_dim=EMBEDDING_DIM),
        training_kwargs=dict(num_epochs=NUM_EPOCHS, batch_size=BATCH_SIZE),
        random_seed=42,
        device='cpu',  # Use CPU for broader compatibility
    )

    print("Training complete.")

    # Get the trained model
    model = pipeline_result.model

    # Extract entity embeddings
    entity_embeddings = model.entity_representations[0]

    # Get the mapping from entity labels to IDs
    entity_to_id = tf.entity_to_id

    # Create a DataFrame to store embeddings
    embedding_data = []
    for entity, entity_id in entity_to_id.items():
        embedding_vector = entity_embeddings(torch.tensor([entity_id])).detach().cpu().numpy().flatten()
        embedding_data.append([entity] + list(embedding_vector))

    embedding_columns = ['node_id'] + [f'emb_{i}' for i in range(EMBEDDING_DIM)]
    embeddings_df = pd.DataFrame(embedding_data, columns=embedding_columns)

    # Save the embeddings
    output_path = os.path.join(EXPERIMENTS_DIR, OUTPUT_EMBEDDINGS_FILE)
    embeddings_df.to_csv(output_path, index=False)
    print(f"Node embeddings saved to {output_path}")

# --- Main Execution ---

if __name__ == "__main__":
    train_and_save_embeddings()
