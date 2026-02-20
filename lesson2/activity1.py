import numpy as np
import matplotlib.pyplot as plt

X = np.array([1,2,3,4,5], dtype=float)
y = np.array([50,55,65,70,75], dtype=float)

def plot_line(m, b):
    predictions = m*X + b
    plt.scatter(X, y)
    plt.plot(X, predictions)
    plt.title(f'm={m}, b={b}')
    plt.show()

plot_line(7.5, 40)