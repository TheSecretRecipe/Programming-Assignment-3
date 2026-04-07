import csv
import matplotlib.pyplot as plt

x = []
y = []

with open("runtime_results.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        x.append(int(row["test"]))
        y.append(float(row["time"]))

plt.plot(x, y, marker='o')
plt.xlabel("Test Case")
plt.ylabel("Runtime (s)")
plt.title("HVLCS Runtime")
plt.savefig("runtime_plot.png")
