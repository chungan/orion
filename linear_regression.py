import numpy as np
from training_data import ratings_for_movie, specific_user_rating, all_ratings

def predict(userID, movieID, all_ratings):
    '''
    Predicts a user's rating for a movie.
    @param userID: the Netflix-assigned ID for the user
    @type userID: int (between 1 to 2649429, inclusive)
    @param movieID: the Netflix-assigned ID for the relevant movie
    @type movieID: int (between 1 and 17770, inclusive)
    @param all_ratings: the ndarray returned by calling all_ratings
    @type all_ratings: numpy.ndarray

    @return: the user's predicted rating for the movie
    @type: float (between 1.0 and 5.0, inclusive)
    '''
    main_user_ratings = all_ratings[all_ratings[:, 1] == userID]
    true_ratings = main_user_ratings[:, 2] #the b-vector
    main_movie_ratings = ratings_for_movie(movieID)
    all_movie_ratings = [all_ratings[all_ratings[:, 0] == m] for m in main_user_ratings[:, 0]]
    all_relevant_ratings = []
    print('Generating a %d x %d matrix'%(len(main_user_ratings), len(main_movie_ratings)))
    for (movie, user, rating, date) in main_movie_ratings:
        ratings = [specific_user_rating(user, m) for m in all_movie_ratings]
        all_relevant_ratings.append(ratings)
    all_relevant_ratings = np.array(all_relevant_ratings).T #the A-matrix
    print('Performing regression')
    weights = np.linalg.lstsq(all_relevant_ratings, true_ratings)[0]
    return round(sum(weights * main_movie_ratings[:, 2]), 4)
