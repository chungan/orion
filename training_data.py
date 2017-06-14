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
    #movie_column = np.zeros((ratings.shape[0], 1)) + movieID
    movie_column = np.full((ratings.shape[0], 1), movieID)
    return np.concatenate((movie_column, ratings), axis=1)

def all_ratings():
    '''
    Queues all ratings provided by netflix

    @return: an array containing rating data for all 17770 movies
    @type: numpy.ndarray
    '''
    return np.concatenate([ratings_for_movie(i) for i in range(1, 17770)])
