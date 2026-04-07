import subprocess
import time
import csv

results = []

for i in range(1, 11):
    fname = f"data/input{i}.in"
    start = time.time()
    subprocess.run(["./hvlcs"], stdin=open(fname), stdout=subprocess.DEVNULL)
    end = time.time()
    results.append((i, end - start))

with open("runtime_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["test", "time"])
    writer.writerows(results)
