from recommender.utils import load_movie_data, load_ratings_data
from recommender.content_recommender import ContentRecommender
from recommender.collaborative_recommender import CollaborativeRecommender

def run():
    movie_df = load_movie_data()
    ratings_df = load_ratings_data()

    print("Content-Based Recommendations:")
    content_rec = ContentRecommender(movie_df)
    print(content_rec.recommend("Toy Story (1995)"))

    print("\nCollaborative Filtering Recommendations:")
    collaborative_rec = CollaborativeRecommender(ratings_df)
    print(collaborative_rec.recommend(user_id=1, movies_df=movie_df))

if __name__ == '__main__':
    run()