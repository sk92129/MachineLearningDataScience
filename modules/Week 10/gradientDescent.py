import numpy as np


def gradient_des(x, y):
    m_curr = 0
    b_curr = 0
    iterations = 10000
    n = len(x)
    learning_rate = 0.01
    for i in range(iterations):
        y_hat = m_curr * x + b_curr
        mse = (1/n) * sum( [diff_y**2 for diff_y in (y-y_hat)])
        m_derivative = -(2/n) * sum( x * ( y-y_hat))
        b_derivative = -(2/n) * sum( y-y_hat)
        m_curr = m_curr - learning_rate * m_derivative
        b_curr = b_curr - learning_rate * b_derivative
        print("m : {}, b: {}, mse: {} iteration: {}".format(m_curr, b_curr, mse, i))


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_des(x, y)
