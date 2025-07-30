import pandas as pd

def load_movie_data():
    return pd.read_csv('data/movies.csv')

def load_ratings_data():
    return pd.read_csv('data/ratings.csv')  # must contain: userId, movieId, rating