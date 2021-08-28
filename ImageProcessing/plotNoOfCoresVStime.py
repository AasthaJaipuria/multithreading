import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
for line in open('data2multi.txt', 'r'):
    lines = [i for i in line.split()]
    x.append(lines[0])
    y.append(float(lines[1]))

plt.title("Change of time with increasing number of threads")
plt.xlabel('No. of Threads')
plt.ylabel('Time in seconds')
plt.yticks(np.arange(min(y),max(y)+1,2))
plt.plot(x, y, marker='o', c='g')

plt.show()