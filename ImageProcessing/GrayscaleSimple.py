import cv2
import glob
import time

#for all images in folder "photos", process 100 images at a time
# for first 100 images: 
images_path = glob.glob('C:/Users/lenovo/Desktop/Open CV/photos/*jpg')
detail = open('data1simple.txt', 'w')

start = time.time()
j=0
for image in images_path:
    if j<100:
        img = cv2.imread(image)
        cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        j+=1
    else:
        break
t = time.time()-start
detail.write('100 ')
detail.write(str(t))
print('100 ', t)

start = time.time()
j=0
for image in images_path:
    if j<200:
        img = cv2.imread(image)
        cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        j+=1
    else:
        break
t = time.time()-start
detail.write('\n200 ')
detail.write(str(t))
print('\n200 ', t)

start = time.time()
j=0
for image in images_path:
    if j<300:
        img = cv2.imread(image)
        cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        j+=1
    else:
        break
t = time.time()-start
detail.write('\n300 ')
detail.write(str(t))
print('\n300 ', t)

start = time.time()
j=0
for image in images_path:
    if j<400:
        img = cv2.imread(image)
        cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        j+=1
    else:
        break
t = time.time()-start
detail.write('\n400 ')
detail.write(str(t))
print('\n400 ', t)

start = time.time()
j=0
for image in images_path:
    if j<500:
        img = cv2.imread(image)
        cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        j+=1
    else:
        break
t = time.time()-start
detail.write('\n500 ')
detail.write(str(t))
print('\n500 ', t)

start = time.time()
j = 0
for image in images_path:
    if j<592:
        img = cv2.imread(image)
        cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        j+=1
    else:
        break
t = time.time()-start
detail.write('\n591 ')
detail.write(str(t))
print('\n591 ', t)

detail.close()