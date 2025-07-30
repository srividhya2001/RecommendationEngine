import pandas as pd
from scipy.sparse.linalg import svds
import numpy as np

class CollaborativeRecommender:
    def __init__(self, ratings_df):
        self.ratings_df = ratings_df
        self.user_item_matrix = self._build_matrix()
        self.user_pred = self._train_model()

    def _build_matrix(self):
        return self.ratings_df.pivot(index='userId', columns='movieId', values='rating').fillna(0)

    def _train_model(self):
        matrix = self.user_item_matrix.values
        u, s, vt = svds(matrix, k=20)
        s_diag_matrix = np.diag(s)
        return np.dot(np.dot(u, s_diag_matrix), vt)

    def recommend(self, user_id, movies_df, top_n=5):
        user_idx = self.user_item_matrix.index.get_loc(user_id)
        sorted_idx = np.argsort(-self.user_pred[user_idx])
        movie_ids = self.user_item_matrix.columns[sorted_idx]
        already_rated = self.ratings_df[self.ratings_df['userId'] == user_id]['movieId'].values
        recommendations = [mid for mid in movie_ids if mid not in already_rated][:top_n]
        return movies_df[movies_df['movieId'].isin(recommendations)]['title'].tolist()