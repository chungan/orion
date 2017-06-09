import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import datestr2num

def plot_rating_by_users(data):
    '''
    Plot a chart of ratings(Y-axis) by users (X-axis).

    @param data: an ndarray with entries of (UserID, Rating, Date)
    @type data: numpy.ndarray
    '''
    xx = data[:, 0]
    yy = data[:, 1]

    plt.title('Rating by Users')
    plt.xlabel('User ID')
    plt.ylabel('Rating')
    plt.scatter(xx, yy, marker='o', color='black')
    plt.show()

def plot_rating_histogram(data):
    '''
    Plot the histogram of ratings.

    @param data: an ndarray with entries of (UserID, Rating, Date)
    @type data: numpy.ndarray
    '''
    xx = data[:, 1]
    mean = np.sum(xx)/float(xx.size)

    plt.title('Rating Histogram: Mean=%.1f'%mean)
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.hist(xx, bins=[1,2,3,4,5,6], normed=0, histtype='bar', facecolor='green', align='left', rwidth=0.8, alpha=0.75)
    plt.grid(True, axis='y')
    plt.show()


if __name__ == "__main__":
    data = np.loadtxt('mv_0000001.txt', skiprows=1, delimiter=',', dtype='int',
                      converters={2: lambda s: datestr2num(s.decode("utf-8"))})
    plot_rating_by_users(data)
    plot_rating_histogram(data)
