import time
import concurrent.futures

detail = open('dataMulti.txt', 'w')

def task(filename):
    f = open(filename)
    f.read().upper()
    f.close()

for i in range (1, 11):
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=i) as executor:
        for j in range(1, 1001):
            executor.submit(task, 'file_{}.txt'.format(j))
    t = time.time()-start
    detail.write(str(i))
    detail.write(' ')
    detail.write(str(t))
    detail.write('\n')
    print(i, ' ', t)

detail.close()

