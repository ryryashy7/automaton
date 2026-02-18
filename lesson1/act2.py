import numpy as np

hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(hours)

print('Add 2 hours:', hours + 2)
print('Average study time:', np.mean(hours))

import matplotlib.pyplot as plt

scores = np.array([50, 55, 65, 70, 80, 96, 97, 89, 91, 93])

plt.scatter(hours, scores)
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.title('Study Time vs Test Score')
plt.show()