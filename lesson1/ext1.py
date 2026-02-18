import numpy as np

temp = np.array([22, 24, 19, 23, 25, 21])
print(temp)
print("Average temperature: ", np.mean(temp))
temp2 = temp + 1
print(temp2)
print("Average temperature with 1 degree added: ", np.mean(temp2))