import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 8), facecolor="#c1f1f1")

for i in range(1, 5):
    df = pd.read_excel(f"./argo-files/{i}.xlsx")
    x = df["T"]
    y = df["P"]*(10**4)/1027/9.8

    if str(i) == "1":
        plt.plot(x, y, label="spring")
    elif str(i) == "2":
        plt.plot(x, y, label="summer")
    elif str(i) == "3":
        plt.plot(x, y, label="fall")
    else:
        plt.plot(x, y, label="winter")

plt.title("Vertical Seawater Temp",
          family="sans-serif", size=25, pad=15)

plt.ylim(810, 0)
plt.xlim(0, 25)
plt.xlabel("temperature(°C)", labelpad=10, size=15)
plt.ylabel("depth(m)", labelpad=10, size=15)


plt.show()