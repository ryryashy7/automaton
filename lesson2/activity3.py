import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
np.random.seed(0)
# Create data
X = np.linspace(0, 10, 30)
true_line = 3*X + 5
noise = np.random.normal(0, 3, 30)
y = true_line + noise
# Fit regression
model = LinearRegression()
model.fit(X.reshape(-1,1), y)
predictions = model.predict(X.reshape(-1,1))
m_normal = model.coef_[0]
b_normal = model.intercept_
error_normal = mean_squared_error(y, predictions)
print("Normal Data:")
print("Slope (m):", round(m_normal, 3))
print("Intercept (b):", round(b_normal, 3))
print("MSE:", round(error_normal, 3))
plt.scatter(X, y)
plt.plot(X, predictions)
plt.title("Normal Noise")
plt.show()

X_outlier = np.append(X, 9)
y_outlier = np.append(y, 50)
model2 = LinearRegression()
model2.fit(X_outlier.reshape(-1,1), y_outlier)
predictions2 = model2.predict(X_outlier.reshape(-1,1))
m_outlier = model2.coef_[0]
b_outlier = model2.intercept_
error_outlier = mean_squared_error(y_outlier, predictions2)
print("With Outlier:")
print("Slope (m):", round(m_outlier, 3))
print("Intercept (b):", round(b_outlier, 3))
print("MSE:", round(error_outlier, 3))
plt.scatter(X_outlier, y_outlier)
plt.plot(X_outlier, predictions2)
plt.title("With One Outlier")
plt.show()