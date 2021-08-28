import cv2
import time
import glob
import concurrent.futures

images_path = glob.glob('C:/Users/lenovo/Desktop/Open CV/photos/*jpg')
detail = open('data2multi.txt', 'w')


def task(image):
    img = cv2.imread(image)
    cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

for i in range (1, 11):
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=i) as executor:
        for image in images_path:
            executor.submit(task, image)
    t = time.time()-start
    print(i, ' ', t)
    detail.write(str(i))
    detail.write(' ')
    detail.write(str(t))
    detail.write('\n')


