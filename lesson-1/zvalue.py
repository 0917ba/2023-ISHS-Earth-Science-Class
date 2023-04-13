import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize = (8, 5))

x = np.random.random(200)
y = np.arange(0, 100, 0.5)
z = np.arange(0, 100, 0.5)

plt.scatter(x, y, c=z, cmap = 'hsv')

plt.colorbar(ticks = [0, 50, 99])
#다음시간에 colorbar에 들어가는 인자 해야함!

plt.show()