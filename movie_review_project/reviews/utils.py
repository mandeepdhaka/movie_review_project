import pandas as pd
from surprise import SVD, Dataset, Reader, accuracy
from surprise.model_selection import train_test_split

from .models import Review


def get_movie_recommendations(user_id, num_recommendations=10):
    # Fetch reviews
    reviews = pd.DataFrame(list(Review.objects.all().values('user_id', 'movie_id', 'rating')))

    # Define the reader
    reader = Reader(rating_scale=(1, 10))

    # Load the dataset
    data = Dataset.load_from_df(reviews[['user_id', 'movie_id', 'rating']], reader)
    trainset, testset = train_test_split(data, test_size=0.2)

    # Train the model
    model = SVD()
    model.fit(trainset)

    # Predict ratings for all movies for the given user
    movie_ids = reviews['movie_id'].unique()
    predictions = [model.predict(user_id, movie_id) for movie_id in movie_ids]

    # Sort predictions by estimated rating
    predictions.sort(key=lambda x: x.est, reverse=True)

    # Get top N recommendations
    top_predictions = predictions[:num_recommendations]
    recommended_movie_ids = [pred.iid for pred in top_predictions]

    return recommended_movie_ids
