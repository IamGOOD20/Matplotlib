# In this lesson, we will learn how to indicate the faces of the axes, that is, number the figure,
# this is done automatically with the creation of the graph, but there are exceptions.
# ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))

import numpy as np
import matplotlib.pyplot as plt
import matplotlib



matplotlib.use('Qt5Agg')

#fig = plt.figure(figsize=(7, 4))
#ax = fig.add_subplot()
#ax.plot(np.arange(1, 5, 0.25))


# ax.set(xlim=(-5, 30), ylim=(-1, 6))
# ax.set_xlim(-5, 30)
# ax.set_ylim(-1, 6)

# ax.set_xlim(xmin=-5, xmax=10)
# ax.set_ylim(ymin=-1, ymax=10)

# plt.xlim(-1, 20)
# plt.ylim(-1, 6)
#
# plt.show()


# position of labels on the coordinate axes
# set_major_locator() large grid
# set_minor_locator() small grid
# matplotlib.ticker.Locator

from matplotlib.ticker import NullLocator, LinearLocator, MultipleLocator, IndexLocator, FixedLocator, LogLocator, MaxNLocator

# NullLocator
# lc = NullLocator()
# ax.grid()
# #ax.xaxis.set_major_locator(lc) # creates X-axis grid only
# ax.yaxis.set_major_locator(lc) # creates Y-axis grid only
# plt.show()

# LinearLocator
# ax.yaxis.set_major_locator(LinearLocator(5)) # works with the Y-axis, breaking it into fractional numbers, rarely used
# plt.show()

# MultipleLocator
# ax.xaxis.set_major_locator(MultipleLocator(base=3.5)) # base=3.5, base=1 ... allows you to use the step between the marks on the axes
# ax.grid()
#
# plt.show()

# IndexLocator # numbers the axes depending on the graphics settings
# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot()
# x = np.arange(-np.pi/2, np.pi, 0.1)
# ax.plot(x, np.sin(x))
#
# ax.grid()
# ax.xaxis.set_major_locator(IndexLocator(base=0.5, offset=0.57))
#
#
# plt.show()

# FixedLokator # sets labels to specified values

# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot()
# x = np.arange(-np.pi/2, np.pi, 0.1)
# ax.plot(x, np.sin(x))
#
# ax.grid()
# ax.xaxis.set_major_locator(FixedLocator([-2, -1, 0, 1, 2, 3]))
#
#
# plt.show()

# LogLocator display of logarithmic divisions along the axes

# MaxNLokator splits the coordinate into the specified number of divisions

# minor grid and class usage
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi/2, np.pi, 0.1)
ax.plot(x, np.sin(x))
ax.minorticks_on()
ax.grid(which='major', lw = 2)
ax.grid(which='minor')

# ax.xaxis.set_major_locator(MaxNLocator(7))
ax.xaxis.set_minor_locator(NullLocator())

plt.show()
