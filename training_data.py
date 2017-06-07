import numpy as np

class Rating:
    """A single rating which includes user, movie, date, and rating."""

    def __init__(self, userID, movieID, rating, date):
        self.userID = userID
        self.movieID = movieID
        self.rating = rating
        self.date = date

def ratings_for_movie(movieID):
    '''
    Queues all ratings for a given movieID
    @param movieID: the Netflix-assigned ID for the relevant movie
    @type movieID: int (between 1 and 17770, inclusive)

    @return: an array of Rating objects for that movieID
    @type: numpy.array
    '''
    movieID = str(movieID)
    for _ in range(7 - len(movieID)):
        movieID = "0" + movieID
    movie_file = open("mv_%s.txt"%movieID)

    ratings = np.array([])
    movie_file.readline()
    for line in movie_file:
        rating_params = line.split(",")
        userID = int(rating_params[0])
        rating = int(rating_params[1])
        date = rating_params[2]
        ratings = np.append(ratings, Rating(userID, movieID, rating, date))
    return ratings
