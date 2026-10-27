# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

import matplotlib.pyplot as plt

#From the previous
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]
fig, ax = plt.subplots()
#Code does not know about pink, or Magenta, BUT OF COURSE IT KNOWS PURPLE
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Purples, s=10)

ax.axis([0, 5100, 0, 130000000000])

ax.set_title("Cubes")
#If ya can see them
ax.set_xlabel("Value")
ax.set_ylabel("Cube of Value")

plt.show()