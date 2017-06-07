import numpy as np
import matplotlib.pyplot as plt

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


if __name__ == "__main__":
    data = np.loadtxt('mv_0000001.txt', skiprows=1, delimiter=',', usecols={0,1})
    plot_rating_by_users(data)
