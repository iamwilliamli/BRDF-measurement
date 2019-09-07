import cv2
import time
import numpy as np
from matplotlib import pyplot as plt
import os
from xlwt import Workbook
# 引入相机矩阵
import recammat
mtx, dist = recammat.recammat()
print(mtx)



# 显示图像，按下s键时开始采集十秒内的十张照片
camera = int(1)# 使用webcam：1
i = 0
j = int(input('目前最后的数据：(重新开始输入0, 如果没有的话输入目前测量的最后数据号）： ')) # 如果没有的话输入目前测量的最后数据值
# 数据进行excel表格保存
wb = Workbook()
sheet1 = wb.add_sheet('Brightness data')
sheet1.write(0, 0, 'Picture Number')
sheet1.write(0, 1, 'Brightness')
while (1):
    cap = cv2.VideoCapture(camera)
    # cap.set(cv2.CAP_PROP_EXPOSURE, 0) #useless

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #划线
    cv2.line(gray, (0, 240), (640, 240), (255, 0, 0), 5)# 横线
    cv2.line(gray, (320, 0), (320, 480), (255, 0, 0), 5)# 竖线

    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == ord('s'):
        for i in range(0,10):
            cap = cv2.VideoCapture(camera)
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite('/Users/William/brdfm/test_photo/test ' + str(i) + '.jpg', gray)
            time.sleep(0.1)
        # 降噪算法：进行均值运算
        sumpic = np.zeros((480, 640, 3)) # 720 1280  480 640
        for i in range(0, 10):
            img = cv2.imread('/Users/William/brdfm/test_photo/test ' + str(i) + '.jpg')
            sumpic = sumpic + img
        sumpic = sumpic / 10

        h, w = sumpic.shape[:2]
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
        # undistort
        dst = cv2.undistort(sumpic, mtx, dist, None, newcameramtx)
        x, y, w, h = roi
        dst = dst[y:y + h, x:x + w]
        
        blinn = dst(240,320)



        cv2.imwrite('/Users/William/brdfm/test_photo/final ' + str(j) + '.jpg', dst)
        # 计算一张图片的亮度值
        print("Sum of arr(float32) : ", np.sum(sumpic, dtype=np.float32))
        # 图片的亮度 float类型
        abs_bright = np.sum(sumpic, dtype=np.float32)
        print(sumpic)



        sheet1.write(int(j)+1 , 0, 'final ' + str(j) + '.jpg')
        sheet1.write(int(j)+1, 1, str(float(abs_bright)))
        wb.save('brightness data.xls')

        cv2.destroyAllWindows()
        j = j+1
    cv2.imshow("capture", gray)
    # 收集图片合成销毁
    try:
        for i in range(0, 10):
            os.remove('/Users/William/brdfm/test_photo/test ' + str(i) + '.jpg')
    except FileNotFoundError:
        print("别墨迹，赶紧拍摄！")
cap.release()


