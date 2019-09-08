import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,20)

y1 = x**2.0

y2 = x**1.5

'''
plt.plot(Abscissa, ordinate,"bo-",linewidth="",markersize="",label="")
"bo-":The shape of the point of the curve
linewidth:The distance from the point on the curve
markersize:The size of the point on the curve
label:Description of the curve
'''
plt.plot(x,y1,"bo-",linewidth=2,markersize=12,label="First")
plt.plot(x,y2,"gs-",linewidth=2,markersize=12,label="Sceond")

#Label corresponding to horizontal and vertical coordinates
plt.xlabel("X")
plt.xlabel("Y")
plt.show()

'''
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