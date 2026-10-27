# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

import matplotlib.pyplot as plt

'''
#For cubed values

cubes = [1, 8, 27, 64, 125]
fig, ax = plt.subplots()
ax.plot(cubes)
plt.show()

ax.set_title("Cubes")
ax.set_xlabel("Value")
ax.set_ylabel("Cube of Value")
'''


# For automating the first 5000

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

ax.axis([0, 5100, 0, 130000000000])

ax.set_title("Cubes")
#If ya can see them
ax.set_xlabel("Value")
ax.set_ylabel("Cube of Value")

plt.show()