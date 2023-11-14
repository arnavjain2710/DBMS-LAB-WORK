# Q6 Write a Python program to create a plot where x and corresponding y values are as follows: x = [1,2,3,4] and y = [2,4,1,8].

import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [2, 4, 1, 8]
plt.plot(x, y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Line Plot")
plt.show()