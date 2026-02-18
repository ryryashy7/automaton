import numpy as np
import matplotlib.pyplot as plt

exercise = np.array([1, 2, 3, 4, 5])
calories = np.array([200, 250, 300, 360, 420])

plt.plot(exercise, calories, marker='o')
plt.xlabel('Exercise Duration (minutes)')
plt.ylabel('Calories Burned')
plt.title('Exercise Duration vs Calories Burned')
plt.grid()
plt.show()