import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

exercise = np.array([1, 2, 3, 4, 5])
calories = np.array([200, 250, 300, 360, 420])

x = exercise.reshape(-1, 1)
y = calories

model = LinearRegression()
model.fit(x, y)

prediction = model.predict([[6]])
print("Predicted calories burned for 6 hours of exercise:", prediction)

plt.scatter(x,y)
plt.plot(x, model.predict(x), color='red')
plt.xlabel('Exercise Duration (Hours)')
plt.ylabel('Calories Burned')
plt.title('Exercise Duration vs Calories Burned')
plt.grid()
plt.show()