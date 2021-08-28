import cv2
import time
import glob
import concurrent.futures
images_path = glob.glob('C:/Users/lenovo/Desktop/Open CV/photos/*jpg')
detail = open('data3minTime.txt', 'w')

def task(image):
    img = cv2.imread(image)
    cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

lst = [100, 200, 300, 400, 500, 591]
for i in lst:
    j = 0
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for image in images_path:
            if j<i:
                executor.submit(task, image)
            else:
                break
            j+=1
    t = time.time()-start
    print(i, ' ', t)
    detail.write(str(i))
    detail.write(' ')
    detail.write(str(t))
    detail.write('\n')
