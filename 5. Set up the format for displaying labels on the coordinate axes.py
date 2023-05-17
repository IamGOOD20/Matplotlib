# set_xticklabels()
# set_yticklabels()


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter, FormatStrFormatter, FuncFormatter, ScalarFormatter, FixedFormatter

matplotlib.use(backend='Qt5Agg')

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi/2, np.pi, 0.1)

# ax.plot(x, np.sin(x))

# set_major_formatter()
# NullFormatter
# ax.yaxis.set_major_formatter(NullFormatter())

# FormatStrFormatter
# ax.yaxis.set_major_formatter(FormatStrFormatter('%d')) # 'y = %.2f'

# FuncFormatter
# def format0y(x, pos):
#    return f'[{x}]' if x < 0 else f'({x})'
#ax.yaxis.set_major_formatter(FuncFormatter(format0y))

# ScalarFormatter

ax.plot(x, np.sin(x) * 1e5)

ax.xaxis.set_major_formatter(FixedFormatter([-3, -2, 0, 1, 2, 3])) # ['a', 'b', 'c', 'd', 'e' . . . .]

ax.grid()
plt.show()