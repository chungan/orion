import numpy as np

def rms_error(estimated_values, true_values):
    '''
    Compute the Root-Mean-Square Error

    @param estimated_values: an array of estimated values
    @type estimated_values: numpy.array
    @param true_values: an array of the corresponding etrue values
    @type true_values: numpy.array

    @return: root-mean-square error of the given data set
    @rtype: float
    '''
    assert(estimated_values.size == true_values.size)
    num_values = estimated_values.size
    return np.sqrt(np.sum(np.square(estimated_values-true_values))/num_values)

if __name__ == "__main__":
    xx = np.array([1,2,3,4,5])
    yy = np.array([1.1,2.2,3.1,3.8,5.2])
    print("rms error of %s and %s is %f"%(xx, yy, rms_error(xx, yy)))
