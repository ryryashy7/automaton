import numpy as np
import matplotlib.pyplot as plt

hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(hours)

print('Add 2 hours:', hours + 2)
print('Average study time:', np.mean(hours))

scores = np.array([50, 55, 65, 70, 79, 84, 87, 90, 92, 95])

from sklearn.linear_model import LinearRegression
x = hours.reshape(-1, 1)
y = scores

model = LinearRegression()
model.fit(x, y) 

prediction = model.predict([[6]])
print("Predicted score for 6 hours of study:", prediction)

plt.scatter(x,y)
plt.plot(x, model.predict(x), color='red')
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.title('Study Time vs Test Score')
plt.show()