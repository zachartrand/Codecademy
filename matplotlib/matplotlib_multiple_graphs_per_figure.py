"""
Matplotlib course from Codecademy.
"""
# This example shows multiple graphs plotted in the same figure where one
# graph is in the first row and two graphs are in the second row.
from matplotlib import pyplot as plt

x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

plt.subplot(2, 1, 1)
plt.plot(x, straight_line)
plt.title('Straight Line')

plt.subplot(2, 2, 3)
plt.plot(x, parabola)
plt.title('Parabola')

plt.subplot(2, 2, 4)
plt.plot(x, cubic)
plt.title('Cubic')

plt.subplots_adjust(wspace=0.35, hspace=0.4, bottom=0.2)

plt.show()
