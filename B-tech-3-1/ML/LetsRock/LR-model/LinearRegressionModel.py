import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
    # x_train is the i/p variable (size in 1000 square feet)
    # y_train is the target (price in 1000 of $)
    x_train = np.array([1.0, 2.0])
    y_train = np.array([300.0, 500.0])
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
    plt.title("Houseing Prices")
    # set the y-axis label
    plt.ylabel("Price (in 1Ks of $)")
    # set the x-axis label
    plt.xlabel('Size (1K sqft)')
    plt.show()

    w = 200
    b = 100
    print(f"w: {w}")
    print(f"b: {b}")

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
        return f_wb

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