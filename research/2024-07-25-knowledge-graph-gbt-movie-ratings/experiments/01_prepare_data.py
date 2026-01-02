import os
import requests
import zipfile
import pandas as pd

# --- Constants ---
DATASET_URL = "http://files.grouplens.org/datasets/movielens/ml-100k.zip"
ZIP_FILE = "ml-100k.zip"
EXTRACT_DIR = "ml-100k"
OUTPUT_DIR = "research/2024-07-25-knowledge-graph-gbt-movie-ratings/experiments"
OUTPUT_FILE = "movielens_100k.csv"

# --- Functions ---

def download_file(url, destination):
    """Downloads a file from a URL to a destination."""
    print(f"Downloading {url} to {destination}...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes
        with open(destination, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print("Download complete.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        return False

def unzip_file(zip_path, extract_to):
    """Unzips a file to a specified directory."""
    print(f"Extracting {zip_path} to {extract_to}...")
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print("Extraction complete.")
        return True
    except zipfile.BadZipFile as e:
        print(f"Error unzipping file: {e}")
        return False

def process_data(extract_path, output_path):
    """
    Loads the MovieLens 100k data, merges it, and saves it as a single CSV.
    """
    print("Processing data...")
    try:
        # Define paths to the data files
        data_file = os.path.join(extract_path, 'u.data')
        item_file = os.path.join(extract_path, 'u.item')

        # Define column names for the datasets
        ratings_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
        movies_cols = ['movie_id', 'movie_title', 'release_date', 'video_release_date',
                       'imdb_url', 'unknown', 'action', 'adventure', 'animation',
                       'childrens', 'comedy', 'crime', 'documentary', 'drama', 'fantasy',
                       'film_noir', 'horror', 'musical', 'mystery', 'romance', 'sci_fi',
                       'thriller', 'war', 'western']

        # Load the ratings and movies data
        ratings = pd.read_csv(data_file, sep='	', names=ratings_cols, encoding='latin-1')
        movies = pd.read_csv(item_file, sep='|', names=movies_cols, encoding='latin-1')

        # Drop unnecessary columns
        movies = movies.drop(columns=['video_release_date', 'imdb_url'])

        # Merge the two dataframes
        df = pd.merge(ratings, movies, on='movie_id')

        # Save the processed dataframe
        df.to_csv(output_path, index=False)
        print(f"Processed data saved to {output_path}")
        return True
    except FileNotFoundError as e:
        print(f"Error processing data: {e}. Make sure the data files are in the correct directory.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred during data processing: {e}")
        return False

# --- Main Execution ---

if __name__ == "__main__":
    # Create the output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    zip_path = os.path.join(OUTPUT_DIR, ZIP_FILE)
    extract_path = os.path.join(OUTPUT_DIR, EXTRACT_DIR)
    output_csv_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

    # Step 1: Download the dataset
    if download_file(DATASET_URL, zip_path):
        # Step 2: Unzip the file
        if unzip_file(zip_path, OUTPUT_DIR):
            # Step 3: Process the data
            process_data(extract_path, output_csv_path)

            # Optional: Clean up the downloaded zip and extracted folder
            print("Cleaning up...")
            os.remove(zip_path)
            # This is a bit tricky due to nested directories, a simple rmdir won't work.
            # For simplicity, we'll leave the extracted folder for now. A more robust
            # solution would use shutil.rmtree.
            print("Cleanup complete.")
