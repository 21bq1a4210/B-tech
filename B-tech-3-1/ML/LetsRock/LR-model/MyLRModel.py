import numpy as np
from matplotlib import pyplot as plt

size = [2104, 1000, 1416, 1534, 852, 3000, 2523, 2750]
price = [460, 150, 232, 351, 176, 720, 525, 623]
array = np.array([size, price])


def compute_model_output(x, w, b):
    '''
    :param x: x(ndarray (m,)): Data, m examples
    :param w, b(scalar): model parameters
    :return: y (ndarray (m,)): target values
    '''
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b
    print(f'f_wb is :{f_wb}')
    return f_wb


def calc_w_b(x, y):
    '''
    :param x: x_train is the i/p variable
    :param y: y_train is the target
    :return: w, b

    Regression Eq of Y on X:
        Σy = w * Σx + n * b
        Σxy = w * Σx^2 + b * Σx
    '''

    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x_2 = np.sum(x ** 2)
    n = len(x)

    A = np.array([[n, sum_x], [sum_x, sum_x_2]])
    B = np.array([sum_y, sum_xy])

    # Solve the system of equations
    solution = np.linalg.solve(A, B)

    return solution

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

if __name__ == "__main__":
    # x_train is the i/p variable (size in 1000 square feet)
    # y_train is the target (price in 1000 of $)
    x_train = array[0]
    y_train = array[1]
    print(f"x_train = {x_train}")
    print(f"y_train = {y_train}")
    print()

    # m is the no.of training examples
    m = x_train.shape[0]
    print(f"no.of training examples is: {m}")
    print()

    # m is the no.of training examples
    m = len(x_train)
    print(f"No.of training examples is: {m}")
    print()

    i = 0 # change this to 1 to see (x^q, y^2)
    x_i = x_train[i]
    y_i = y_train[i]
    print(f"(x^({i}),y^({i}) = ({x_i}, {y_i})")
    print()

    # Plot the data points
    plt.scatter(x_train, y_train, marker='x', c='r')
    # set the title
    plt.title("Housing Prices")
    # set the y-axis label
    plt.ylabel("Price (in 1Ks of $)")
    # set the x-axis label
    plt.xlabel('Size (1K sqft)')
    plt.show()

    b, w = calc_w_b(x_train, y_train)
    print(f"cost function of {w, b} is {compute_cost(x_train, y_train, w, b)}")
    tmp_f_wb = compute_model_output(x_train, w, b)

    # Plot our model prediction
    plt.plot(x_train, tmp_f_wb, c='b', label='Our Prediction')

    # Plot the data points
    plt.scatter(x_train, y_train, marker='x', c='r', label='Actual Values')

    # set the title
    plt.title("housing prices")
    # set the y-axis label
    plt.ylabel('Price (in 1000s of dollars)')
    # Set the x-axis label
    plt.xlabel('Size (1000 sqft)')
    plt.legend()
    plt.show()