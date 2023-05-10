import matplotlib
import matplotlib.pyplot as plt

#matplotlib.use('Qt5Agg') # change baskend
print(matplotlib.get_backend())

plt.plot([1, 2, -6, 0, 4])
plt.show()