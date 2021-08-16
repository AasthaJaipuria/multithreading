import os
import random

a = open('text_file.txt', 'r')
t = a.read()
for i in range(1, 1001):
    f = open('file_{}.txt'.format(i), 'w')
    #size = 2 * 1024 * 1024 = 2 MB = 2097152
    # 5MB = 5 * 1024 * 1024 = 5242880
    randomNo = random.randint(2097152, 5242880)
    while os.stat('file_{}.txt'.format(i)).st_size < randomNo:
        f.write(t)
    #a = open('file_{}.txt'.format(i), 'r')
    b = os.stat('file_{}.txt'.format(i)).st_size,'bytes'
    print('file_{}.txt: '.format(i),b)





