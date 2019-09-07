import cv2
import time
import numpy as np
from matplotlib import pyplot as plt
import os


# 显示图像，按下s键时开始采集十秒内的十张照片
camera = int(1)  # 使用webcam：1
i = 0
j = 0

while (1):
    cap = cv2.VideoCapture(camera)
    # cap.set(cv2.CAP_PROP_EXPOSURE, 0) #useless

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 划线
    cv2.line(gray, (0, 240), (640, 240), (255, 0, 0), 5)  # 横线
    cv2.line(gray, (320, 0), (320, 480), (255, 0, 0), 5)  # 竖线

    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == ord('s'):
        for i in range(0, 1):
            cap = cv2.VideoCapture(camera)
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite('/Users/William/brdfm/biao/sample ' + str(j) + '.jpg', gray)
        # 降噪算法：进行均值运算
        cv2.destroyAllWindows()
        j = j + 1
    cv2.imshow("capture", gray)
    # 收集图片合成销毁
cap.release()


