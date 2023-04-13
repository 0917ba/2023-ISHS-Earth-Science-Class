import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.random(300)
y1 = np.random.random(300)

x2 = np.random.random(100)
y2 = np.random.random(100)

plt.scatter(x1, y1, color = 'tomato', alpha = 0.5, edgecolor = 'r', s = 100)
plt.scatter(x2, y2)

plt.show()