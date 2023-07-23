import matplotlib.pyplot as plt
import numpy as np
#from lab_utils_uni import plt_intuition, plt_stationary, plt_update_onclick, soup_bowl

x_train = np.array([1.0, 2.0])      #(size in 1k sqf)
y_train = np.array([300.0, 500.0])  #(price in 1K's of $)

def compute_cost(x, y, w, b):
    '''
        J(w,b) = (1/2m)*((i=0Σm-1)f(x)-y)**2
    '''
    '''
    :param x: (ndarray (m,)): Data, m examples
    :param y: (ndarray (m,)): target values
    :param w, b: (scalar): model parameters
    :return: total_cost (float): The cost of using w,b as the parameters for linear regression
               to fit the data points in x and y
    '''

    # no.of training examples
    m = x.shape[0]
    cost_sum = 0

    for i in range(m):
        f_wb = w * x[i] + b
        cost = (f_wb - y[i]) ** 2
        cost_sum += cost
    total_cost = (1/(2*m)) * cost_sum
    return total_cost

x_train = [1.0, 1.7, 2.0, 3.0, 3.2]
y_train = [250, 300, 480, 630, 730]

plt.close('all')