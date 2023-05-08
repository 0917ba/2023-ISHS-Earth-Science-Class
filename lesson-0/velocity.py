import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8, 6))

x = np.arange(0, 5, 0.5)


font1 = {'family':'serif', 'size':10}


plt.xlim(0, 4)
plt.ylim(0, 16)

plt.plot(x, x, linestyle = ':', marker = 'o', label='cheap one')
plt.plot(x, x**3, linestyle = '-.', marker = '^', markersize = '15', label='expensive one')

plt.xlabel('time(s)', size=12, loc='center', family='serif')
plt.ylabel('velocity(m/s)', size=12, loc='center', family='serif')
plt.title('Velocity of Car', size=20, loc='center', family='serif')


plt.grid(linestyle='--', linewidth=0.5)

plt.legend(ncol=2, prop=font1)

plt.show()