from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('logistical_regression/rain.csv')
x = data['Sunshine'].to_numpy()
y = data['RainTomorrow'].to_numpy()

logistic_reg = LogisticRegression()
logistic_reg.fit(x.reshape(-1,1), y)

beta0 = logistic_reg.intercept_
beta1 = logistic_reg.coef_[0]

x_model = np.linspace(0, 10, 50)
y_model = 1/(1 + np.exp(-(beta0 + beta1 * x_model)))

plt.figure(figsize=(4, 4))
plt.scatter(x, y)
plt.plot(x_model, y_model, color='red')
plt.xlabel('Sunshine')
plt.ylabel("Rain Tommorow")
plt.xlim([0, 10])