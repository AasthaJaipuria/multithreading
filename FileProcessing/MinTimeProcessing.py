import time
import concurrent.futures

detail = open('dataMinTime.txt', 'w')

def task(filename):
    f = open(filename)
    f.read().upper()
    f.close()

lst = [201, 401, 601, 801, 1001]
for i in lst:
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for j in range(1, i):
            executor.submit(task, 'file_{}.txt'.format(j))
    t = time.time()-start
    detail.write(str(i-1))
    detail.write(' ')
    detail.write(str(t))
    detail.write('\n')
    print(i-1, ' ', t)

detail.close()

