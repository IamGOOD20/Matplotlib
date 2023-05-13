import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Qt5Agg')

# display 1g 2g 3g
# This code displays 3 graphs in 1 window
# plt.subplot(1, 3, 1)
# plt.plot(np.random.random(10))
# plt.grid()
# plt.subplot(1, 3, 2)
# plt.plot(np.random.random(10))
# plt.grid()
# plt.subplot(1, 3, 3)
# plt.plot(np.random.random(10))
# plt.grid() # grid will be in last graph only!
# plt.show()

# display 1g 2g 3g
# Grid creation in every window

# ax1 = plt.subplot(2, 3, 1)
# plt.plot(np.random.random(10))
#
# ax2 = plt.subplot(2, 3, 2)
# plt.plot(np.random.random(10))
#
# ax3 = plt.subplot(2, 3, 3)
# plt.plot(np.random.random(10))
#
# ax4 = plt.subplot(2, 1, 2)
# plt.plot(np.random.random(10))
#
# ax1.grid()
# ax2.grid()
# ax3.grid()
# ax4.grid()
# plt.show()

# display 1   2   3
#             4

# ax1 = plt.subplot(2, 3, 1)
# plt.plot(np.random.random(10))
#
# ax2 = plt.subplot(2, 3, 2)
# plt.plot(np.random.random(10))
#
# ax3 = plt.subplot(2, 3, 3)
# plt.plot(np.random.random(10))
#
# ax4 = plt.subplot(2, 1, 2)
# plt.plot(np.random.random(10))
#
# ax1.grid()
# ax2.grid()
# ax3.grid()
# ax4.grid()
# plt.show()

# when we need to display multiple coordinate graphs in one form
# subplots(nrows, ncols)



# f, ax = plt.subplots(2, 2) # display 4 empty forms

# using f we can:
# f.set_size_inches(7, 4)     # size
# f.set_facecolor('#eee')     # color
# more options can be found in the official document

# add graphs
# using ax we can:
# ax[0, 0].plot(np.arange(0, 5, 0.2))
# ax[0, 0].grid() # add
# ax[0, 1].plot(np.arange(5, 0, -0.2))
# ax[0, 1].grid()

# creates a figure in a separate window 7" x 4"
# fig = plt.figure(figsize=(7, 4))
# add graph
# 1
#plt.plot(np.arange(0, 5, 0.2))
# 2
# ax1 = fig.add_axes([0.0, 0, 1.0, 1.0])
# ax1.plot(np.arange(0, 5, 0.2)) # size for the whole
# plt.show() # display 4 empty forms
# 3
# ax1 = fig.add_subplot(1, 3, 1)
# ax1.plot(np.arange(0, 5, 0.2))
# plt.show()

# 4
f, ax = plt.subplots()
f.set_size_inches(7, 4)     # size
f.set_facecolor('#eee')     # color
ax.plot(np.arange(0, 5, 0.2))
plt.show()