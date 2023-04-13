import matplotlib.pyplot as plt

x = [10, 20, 30, 40, 50]
y = [60, 70, 80, 90, 100]

err = [5, 6, 9, 2, 11]

plt.errorbar(x, y, err, color = 'k', marker = 's', markersize = 15, markerfacecolor = 'r', markeredgecolor = 'r',
             capsize = 4, linewidth = 2)

plt.show()