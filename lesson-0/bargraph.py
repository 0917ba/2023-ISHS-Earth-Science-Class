import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8, 6))

price = np.array([9900, 11000, 22000])
# x = np.arange(0, 3, 1)
y = np.arange(0, 3, 1)
year = [1990, 2000, 2010]


# plt.bar(x, price, width=0.4, color=['orange', 'red', 'green'])
plt.barh(y, price, height=0.4, color=['orange', 'red', 'green'])

# plt.xticks(x, year)
plt.yticks(y, year)

plt.title('Price Of Chicken')

# plt.grid(axis='y')
plt.grid(axis='x')

plt.show()