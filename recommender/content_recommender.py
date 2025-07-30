import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class ContentRecommender:
    def __init__(self, movie_df):
        self.movie_df = movie_df
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.movie_df['genres'] = self.movie_df['genres'].fillna('')
        self.tfidf_matrix = self.tfidf.fit_transform(self.movie_df['genres'])
        self.similarity_matrix = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)

    def recommend(self, title, top_n=5):
        if title not in self.movie_df['title'].values:
            return []

        idx = self.movie_df[self.movie_df['title'] == title].index[0]
        sim_scores = list(enumerate(self.similarity_matrix[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
        movie_indices = [i[0] for i in sim_scores]
        return self.movie_df['title'].iloc[movie_indices].tolist()