# This is my work (^_^)
#AGAIN GOING INSANE, WHY CAN'T IT IMPORT, I COPIED IT!!! IT HAD NO PROBLEMS! WHY DOES IT HAVE PROBLEMS!?!?!?!?
# All of this is written by me
# Aaron Cribbin
import matplotlib.pyplot as plt

from random_walk_mod import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=15)
ax.set_aspect('equal')

ax.scatter(0, 0, c='blue', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolors='none', s=100)

plt.show()