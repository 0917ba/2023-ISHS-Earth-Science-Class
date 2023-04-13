import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel(r'./grade.xlsx');

er = ([7, 8, 11, 5, 6, 19, 30], [9, 3, 2, 11, 6, 9, 4])

plt.figure(figsize = (8, 5))

plt.bar(df['student'], df['grade'], color = ['red', 'blue', 'green', 'orange', 'magenta', 'tomato', 'violet'], 
        edgecolor = 'k', linewidth = 1.5, yerr = er, capsize = 3, ecolor = 'grey')

plt.xticks(family = 'serif')
plt.yticks(family = 'serif')

plt.grid(axis = 'y', linestyle = '--')

plt.title('Lee Woo Jin', family = 'serif', weight = 'bold', size = 20)

plt.show()