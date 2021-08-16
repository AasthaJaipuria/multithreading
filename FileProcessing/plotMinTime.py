import matplotlib.pyplot as plt

x = []
y = []
for line in open('dataMinTime.txt', 'r'):
    lines = [i for i in line.split()]
    x.append(lines[0])
    y.append(float(lines[1]))

plt.title("Processing Time of Files using 8 threads")
plt.xlabel('No. of Files Processed')
plt.ylabel('Time in seconds')
plt.yticks(y)
plt.plot(x, y, marker='o', c='g')

plt.show()