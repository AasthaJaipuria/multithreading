import matplotlib.pyplot as plt

x = []
y = []
for line in open('data3minTime.txt', 'r'):
    lines = [i for i in line.split()]
    x.append(lines[0])
    y.append(float(lines[1]))

plt.title("Processing Time of Photos using multithreading")
plt.xlabel('No. of Photos')
plt.ylabel('Time in seconds')
plt.yticks(y)
plt.plot(x, y, marker='o', c='g')

plt.show()