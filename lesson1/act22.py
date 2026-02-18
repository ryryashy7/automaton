import matplotlib.pyplot as plt

scores = np.array([50, 55, 65, 70, 80, 96, 97, 89, 91, 93])

plt.scatter(hours, scores)
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.title('Study Time vs Test Score')
plt.show()