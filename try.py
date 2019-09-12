'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,20)

y1 = x**2.0

y2 = x**1.5



plt.plot(Abscissa, ordinate,"bo-",linewidth="",markersize="",label="")
"bo-":The shape of the point of the curve
linewidth:The distance from the point on the curve
markersize:The size of the point on the curve
label:Description of the curve

plt.plot(x,y1,"bo-",linewidth=2,markersize=12,label="First")
plt.plot(x,y2,"gs-",linewidth=2,markersize=12,label="Sceond")

#Label corresponding to horizontal and vertical coordinates
plt.xlabel("X")
plt.xlabel("Y")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from xlrd import open_workbook
from pylab import *

center_br=[]
view_angle=[]
wb = open_workbook('/Users/William/brdfm/brightness data.xls')
for s in wb.sheets():
    for row in range(1, s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        center_br.append(values[2])
        view_angle.append(values[4]) # 之后要调整为第三列 values[3]

plt.plot(view_angle, center_br, label="Curve",linewidth=1)
plt.title("Incident Azimuth angle: 62.05")
plt.legend()

ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.xlabel("Viewing angle")
plt.ylabel("Pixel Value")


plt.show()
'''

import cv2
import time
import numpy as np
from matplotlib import pyplot as plt
import os
from xlwt import Workbook
import calculator
import brdffunc

# Math Calculation Vector form
theta_i = float(input('输入光源天顶角角度: ')) # Input the Zenith angle of the light source
theta_r = float(input('输入相机天顶角角度： ')) # input the Zenith angle of the camera
phi_i = 0 #光源方位角固定为0 Azimuth angle of light source is fixed to zero
phi_r = float(input('输入相机方位角: '))
incident_vector = calculator.incident(theta_i, phi_i) # 入射光向量
camera_vector = calculator.view(theta_r, phi_r) # 出射光线向量
normal = calculator.normal() # 平面法向量
half_angle = calculator.half(theta_i, phi_i, theta_r, phi_r) # 半角向量 H
delta_angle = calculator.delta(half_angle, normal)
alpha_angle = calculator.alpha(incident_vector, camera_vector)
print(alpha_angle)
print(delta_angle)




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
sheet1.write(0, 2, 'Center Value')
sheet1.write(0, 3, 'Incident angle')
sheet1.write(0, 4, 'Reflective angle')

while (1):
    # Math Calculation Vector form
    theta_i = float(input('输入光源天顶角角度: '))  # Input the Zenith angle of the light source 实验时固定值
    theta_r = float(input('输入相机天顶角角度： '))  # input the Zenith angle of the camera 实验时固定值
    phi_i = 0  # 光源方位角固定为0 Azimuth angle of light source is fixed to zero
    phi_r = float(input('输入相机方位角: ')) #注意：垂直的时候进行
    incident_vector = calculator.incident(theta_i, phi_i)  # 入射光向量
    camera_vector = calculator.view(theta_r, phi_r)  # 出射光线向量
    normal = calculator.normal()  # 平面法向量
    half_angle = calculator.half(theta_i, phi_i, theta_r, phi_r)  # 半角向量 H
    delta_angle = calculator.delta(half_angle, normal)
    alpha_angle = calculator.alpha(incident_vector, camera_vector)
    print(alpha_angle)
    print(delta_angle)

    cap = cv2.VideoCapture(camera)
    # cap.set(cv2.CAP_PROP_EXPOSURE, 0) #useless

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #划线
    cv2.line(gray, (0, 240), (640, 240), (255, 0, 0), 5)# 横线
    cv2.line(gray, (320, 0), (320, 480), (255, 0, 0), 5)# 竖线
    #cv2.line(gray, )

    k = cv2.waitKey(1)
    if k == 27:
        break

    for i in range(0,10):
        cap = cv2.VideoCapture(camera)
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('/Users/William/brdfm/test_photo/test ' + str(i) + '.jpg', gray)
        time.sleep(0.1)
    # 降噪算法：进行均值运算
    sumpic = np.zeros((480, 640)) # 720 1280  480 640
    for i in range(0, 10):
        img = cv2.imread('/Users/William/brdfm/test_photo/test ' + str(i) + '.jpg',cv2.IMREAD_GRAYSCALE)
        sumpic = sumpic + img
    sumpic = sumpic / 10


    dst = cv2.undistort(sumpic, mtx, dist, None, mtx)



        # 改变视角、计算图片中心4*4像素
    rows, cols = dst.shape
    center = dst[240,320]
    print(center)





    cv2.imwrite('/Users/William/brdfm/test_photo/final ' + str(j) + '.jpg', dst)
    # 计算一张图片的亮度值
    print("Sum of arr(float32) : ", np.sum(sumpic, dtype=np.float32))
    # 图片的亮度 float类型
    abs_bright = np.sum(sumpic, dtype=np.float32)



    sheet1.write(int(j)+1 , 0, 'final ' + str(j) + '.jpg')
    sheet1.write(int(j)+1, 1, str(float(abs_bright)))
    sheet1.write(int(j) + 1, 2, str(float(center)))

    wb.save('brightness data.xls')

    cv2.destroyAllWindows()
    j = j+1
cv2.imshow("capture", gray)
    # 收集图片合成销毁
try:
    for i in range(0, 10):
        os.remove('/Users/William/brdfm/test_photo/test ' + str(i) + '.jpg')
except FileNotFoundError:
    time.sleep(0)
cap.release()





# Math Calculation Vector form
theta_i = deg2rad(float(input('输入光源天顶角角度: '))) # Input the Zenith angle of the light source
theta_r = deg2rad(float(input('输入相机天顶角角度： '))) # input the Zenith angle of the camera
phi_i = 0 #光源方位角固定为0 Azimuth angle of light source is fixed to zero
phi_r = deg2rad(float(input('输入相机方位角: ')))




incident_vector = incident(theta_i, phi_i) # 入射光向量
camera_vector = view(theta_r, phi_r) # 出射光线向量
normal = normal() # 平面法向量
half_angle = half(theta_i, phi_i, theta_r, phi_r) # 半角向量 H
delta_angle = delta(half_angle, normal)
alpha_angle = alpha(incident_vector, camera_vector)
#print(half_angle)
#print(alpha_angle)
#print(delta_angle)

print(delta_angle)
d = b.Beckmann_D(1, delta_angle)
#d = b.CT_D(delta_angle)
#print(d)
f = b.Fresnel(0.919, alpha_angle)
#print(f)
g = b.G_shadow(alpha_angle, delta_angle, theta_r, theta_i)
#print(g)
known = b.BRDF_known(d, f, g, theta_i, theta_r)
print(known)