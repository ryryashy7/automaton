import numpy as np
import matplotlib.pyplot as plt

X = np.array([4.5, 8, 1.5, 3.5, 5.5, 3, 6.5], dtype=float)
y = np.array([60,  80, 31, 54, 58, 30, 78], dtype=float)

# Export data as a tuple/list for testactivity.py to use
data = (X, y)

def plot_line(m, b):
    predictions = m*X + b
    plt.scatter(X, y)
    plt.plot(X, predictions)
    plt.title(f'm={m}, b={b}')
    plt.show()

a = 8.55
b = 15.95
plot_line(a, b)

def mse(X, y, m, b):
    predictions = m*X + b
    return np.mean((y - predictions)**2)

print('MSE:', mse(X, y, a, b))