# Augmenting Gradient Boosted Decision Trees with Knowledge Graph Features for Movie Rating Prediction

**Date:** 2024-07-25
**Type:** academic

## Research Question

Does augmenting a Gradient Boosted Decision Tree (e.g., XGBoost) with topological features and embeddings derived from a Knowledge Graph improve rating prediction accuracy compared to using only raw metadata features?

## Executive Summary

Augmenting Gradient Boosted Decision Trees (GBDTs) with features derived from knowledge graphs is a promising approach to improving movie rating prediction accuracy. The research indicates that knowledge graphs can capture complex relationships between entities such as movies, actors, directors, and genres that are not easily represented by raw metadata alone. By using techniques like Graph Neural Networks (GNNs), it is possible to generate dense vector representations (embeddings) of these entities, which can then be used as features in a GBDT model like XGBoost. Additionally, topological features, which describe the structure of the graph, can provide further valuable signals to the model.

The AWS blog series on building a recommendation engine with an IMDb knowledge graph provides a practical, in-depth guide to the entire process, from data preparation and graph creation to training a GNN and using the resulting embeddings. This approach allows for the incorporation of rich, contextual information into the recommendation model, which has the potential to lead to more accurate and personalized recommendations.

## Key Findings

- **Knowledge Graphs for Rich Feature Representation:** Knowledge graphs are an effective way to model the complex and interconnected nature of movie data. They can represent relationships between entities like movies, actors, genres, and keywords, providing a richer source of features than raw metadata alone.
- **Embeddings from Graph Neural Networks:** Graph Neural Networks (GNNs) can be trained on a knowledge graph to produce high-quality embeddings for nodes (e.g., movies, users). These embeddings can be used as input features for a downstream prediction model, such as XGBoost, to improve its performance.
- **Topological Features as Predictive Signals:** In addition to embeddings, topological features derived from the graph's structure can be used as features. These can include metrics like node centrality (e.g., PageRank), which can indicate the importance of a particular movie or actor, and community detection, which can identify groups of related items.
- **Practical Implementation with AWS:** The AWS blog series provides a comprehensive, three-part tutorial on how to build and use a knowledge graph for recommendations using the IMDb dataset. This includes data processing, loading the data into Amazon Neptune, training a GNN model with Neptune ML, and using the resulting embeddings for search and recommendation.

## Sources & References

1. [Power recommendation and search using an IMDb knowledge graph – Part 1](https://aws.amazon.com/blogs/machine-learning/part-1-power-recommendation-and-search-using-an-imdb-knowledge-graph/) - This article provides a detailed guide on how to prepare the IMDb dataset and load it into Amazon Neptune to create a knowledge graph.
2. [The Graph Attention Recommendation Method for Enhancing User Features Based on Knowledge Graphs](https://www.mdpi.com/2227-7390/13/3/390) - This paper discusses a method for improving recommendation systems by using a graph attention mechanism to enhance user features based on a knowledge graph.
3. [Xgboost Tutorial](https://www.kaggle.com/code/yasinnsariyildiz/xgboost-tutorial) - A helpful Kaggle notebook providing a tutorial on how to use XGBoost.

## Code Experiments & Validations

To practically test the research question, a series of Python scripts were created in the `experiments/` directory to build and evaluate a recommendation model.

### Experiment 1: Baseline vs. Augmented XGBoost Model

**Goal:** To quantify the performance improvement of an XGBoost rating prediction model when augmented with knowledge graph-derived features (topological features and embeddings) compared to a baseline model using only raw metadata.

**Method:**
1.  **Data Preparation:** The MovieLens 100K dataset was downloaded and processed into a unified CSV file.
2.  **Graph Construction:** A knowledge graph was built using the `networkx` library, connecting users, movies, and genres. Topological features (degree centrality and PageRank) were calculated for each node.
3.  **Embedding Training:** The `PyKEEN` library was used to train a `TransE` model on the graph, generating 64-dimensional embeddings for all nodes.
4.  **Model Training:** Two XGBoost regressor models were trained to predict movie ratings:
    *   **Baseline Model:** Used only `user_id` and `movie_id` as features.
    *   **Augmented Model:** Used the baseline features plus the calculated topological features and the trained node embeddings for both users and movies.
5.  **Evaluation:** The performance of both models was evaluated on a held-out test set using the Root Mean Squared Error (RMSE) metric.

**Results:**
The experiment demonstrated a clear and significant improvement when using the graph-derived features.

*   **Baseline Model RMSE:** `1.0219`
*   **Augmented Model RMSE:** `0.9488`
*   **Improvement:** The augmented model achieved a **7.15% reduction in RMSE** compared to the baseline.

This result strongly supports the hypothesis that incorporating topological features and embeddings from a knowledge graph can significantly improve the accuracy of a Gradient Boosted Decision Tree model for movie rating prediction.

**Code:** See the scripts in the `experiments/` directory for the full implementation.

**Setup Instructions:**
To replicate this experiment, run the following commands from the repository root:
```bash
# Install all required Python packages
pip install requests pandas networkx scipy pykeen torch xgboost scikit-learn

# Run the experiment scripts in order
python3 research/2024-07-25-knowledge-graph-gbt-movie-ratings/experiments/01_prepare_data.py
python3 research/2024-07-25-knowledge-graph-gbt-movie-ratings/experiments/02_build_graph.py
python3 research/2024-07-25-knowledge-graph-gbt-movie-ratings/experiments/03_train_embeddings.py
python3 research/2024-07-25-knowledge-graph-gbt-movie-ratings/experiments/04_run_experiment.py
```

## Next Steps / Open Questions

- [ ] A deeper investigation into specific topological features that are most effective for movie rating prediction.
- [ ] A study comparing the performance of different GNN architectures for generating movie and user embeddings.
- [ ] An exploration of how to best combine embeddings and topological features with traditional metadata features in an XGBoost model.

---

*Research conducted by Jules | [View notes.md for work log](notes.md)*
