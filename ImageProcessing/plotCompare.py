import matplotlib.pyplot as plt
import numpy as np

# encoding*****
data1 = open('data1simple.txt', 'r', encoding='UTF-8')
data2 = open('data3minTime.txt', 'r', encoding='UTF-8')

files = []
wall_time1 = []
wall_time2 = []

for line in data1:
    inst = [i for i in line.split()]
    files.append(int(inst[0]))
    wall_time1.append(float(inst[1]))

for line in data2:
    inst = [i for i in line.split()]
    wall_time2.append(float(inst[1]))

plt.title("Graph comparing process time with and without multithreading")
plt.xlabel('Number of images')
plt.ylabel('Processing time in seconds')
#plt.xticks(np.arange(0, 21, 1))
plt.yticks(np.arange(min(min(wall_time1), min(wall_time2)), max(max(wall_time1), max(wall_time2)) + 10, 10))

plt.plot(files, wall_time1, marker='o', color='g', label='no multithreading')
plt.plot(files, wall_time2, marker='o', color='b', label='multithreading')

for x, y in zip(files, wall_time1):
    label = "{:.2f}".format(y)
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

for x, y in zip(files, wall_time2):
    label = "{:.2f}".format(y)
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

plt.legend()
plt.show()

data1.close()
data2.close()