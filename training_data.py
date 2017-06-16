import numpy as np
from matplotlib.dates import datestr2num

def ratings_for_movie(movieID):
    '''
    Queues all ratings for a given movieID
    @param movieID: the Netflix-assigned ID for the relevant movie
    @type movieID: int (between 1 and 17770, inclusive)

    @return: an array containing rating data for that movieID
    @type: numpy.ndarray
    '''
    movie_file = 'mv_%07d.txt'%movieID
    ratings = np.loadtxt(movie_file, delimiter=',', skiprows=1,
                      converters={2: lambda s: datestr2num(s.decode("utf-8"))})
    movie_column = np.full((ratings.shape[0], 1), movieID)
    return np.concatenate((movie_column, ratings), axis=1)

def specific_user_rating(userID, movie_ratings):
    '''
    Queues rating for specific user for given movie.
    If doesn't exist, returns average rating for movie.
    @param userID: the Netflix-assigned ID for the user
    @type userID: int (between 1 to 2649429, inclusive)
    @param movie_ratings: ndarray of ratings for one movie
    @type movieID: numpy.ndarray

    @return: a user's rating for the movie, or the average rating
    @type: float
    '''
    if userID in movie_ratings[:, 1]:
        return movie_ratings[movie_ratings[:, 1] == userID][0][2]
    return np.mean(movie_ratings[:, 2])

def all_ratings():
    '''
    Queues all ratings provided by netflix

    @return: an array containing rating data for all 17770 movies
    @type: numpy.ndarray
    '''
    return np.concatenate([ratings_for_movie(i) for i in range(1, 17771)])
