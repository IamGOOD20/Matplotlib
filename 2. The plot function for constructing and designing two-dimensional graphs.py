import matplotlib
import matplotlib.pyplot as plt
import numpy as np


matplotlib.use('Qt5Agg') # change backend
# plt.plot([1, 2, -6, 0, 4])

# will output a square
# x = np.array([1, 1, 5, 5, 1])
# y = np.array([1, 5, 5, 1, 1])
# plt.plot(x, y)
# plt.show()

# create line  graph
# y = np.arange(0, 5, 1)
# x = np.array([i * i for i in y])
# add another line graph
# y2 = [0, 1, 2, 3]
# x2 = [i + 1 for i in y2]

# plt.plot(x, y, x2, y2) # add second graph
# plt.plot(x2, y2)
# plt.grid()
# plt.show()


# How to change the graph line
# 1
# y = np.arange(0, 5, 1)
# x = np.array([i * i for i in y])
# plt.plot(x, y, '--') # '-', '--', '-.', ':'. 'None or '' '
# plt.grid()
# plt.show()

# 2
# y = np.arange(0, 5, 1)
# x = np.array([i * i for i in y])
# lines = plt.plot(x, y)
# # print(lines)
# plt.setp(lines, linestyle='-.')
# plt.grid()
# plt.show()

# How to change the color of graph
# y = np.arange(0, 5, 1)
# x = np.array([i * i for i in y])
# y2 = [0, 1, 2, 3]
# x2 = [i + 1 for i in y2]
# plt.plot(x, y, '--r', x2, y2, 'b:', color=(0, 1, 0, 0.8)) # color='g' !!!! add color for all graphs
#                                     # but we can add color code like #23231CC or a tuple (1, 1, 1, 0,8) # 0.8 transparency
# plt.grid()
# plt.show()

# how to change marker
# y = np.arange(0, 5, 1)
# x = np.array([i * i for i in y])
# y2 = [0, 1, 2, 3]
# x2 = [i + 1 for i in y2]
# plt.plot(x, y, '--r', x2, y2, 'b:D') # marker is like a square
# or
# plt.plot(x, y, 'o--r', x2, y2, 'b:D', marker="+", markerfacecolor='w') # markerfacecolor -- the color inside the marker
# or
# lines = plt.plot(x, y, 'r--o', marker='*', markerfacecolor='w')
# plt.setp(lines[0], linestyle='-.', marker='s', markerfacecolor='b', linewidth=4) # set a lot of parameters for the line of the chart,
#                                                                                  # there are a lot of parameters,
#                                                                                  # see the documentation
# plt.grid()
# plt.show()

# pouring economic graphics

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.cos(x)
plt.plot(x, y)
plt.fill_between(x, y) # this function paints the chart area, it also has additional parameters
                        # you can paint in different colors, choose from which number to start painting

plt.grid()
plt.show()
