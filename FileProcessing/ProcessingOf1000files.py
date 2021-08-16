# code to convert the file text to upper case and to note the process time of 200 files at a time
import time
detail = open('data.txt','w')

start = time.time()
for i in range(1, 200):
    f = open('file_{}.txt'.format(i), 'r')
    f.read().upper()
    f.close()
t = time.time()-start
detail.write('200 ')
detail.write(str(t))

start = time.time()
for i in range(1, 401):
    f = open('file_{}.txt'.format(i), 'r')
    f.read().upper()
    f.close()
t = time.time()-start
detail.write('\n400 ')
detail.write(str(t))
#print(" file 1-400: %s seconds" % (time.time() - start))

start = time.time()
for i in range(1, 601):
    f = open('file_{}.txt'.format(i), 'r')
    f.read().upper()
    f.close()
t = time.time()-start
detail.write('\n600 ')
detail.write(str(t))
#print(" file 1-600: %s seconds" % (time.time() - start))

start = time.time()
for i in range(1, 801):
    f = open('file_{}.txt'.format(i), 'r')
    f.read().upper()
    f.close()
t = time.time()-start
detail.write('\n800 ')
detail.write(str(t))
#print(" file 1-800: %s seconds" % (time.time() - start))

start = time.time()
for i in range(1, 1001):
    f = open('file_{}.txt'.format(i), 'r')
    f.read().upper()
    f.close()
t = time.time()-start
detail.write('\n1000 ')
detail.write(str(t))
#print(" file 1-1000: %s seconds" % (time.time() - start))
detail.close()

