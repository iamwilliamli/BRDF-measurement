import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

incident_angle = input('输入入射天顶角：')
chushetianding = input('输入出射天顶角： ')
chushefangwei = input('输入出射方位角： ')
data_file = pd.read_excel('/Users/William/brdfm/brightness data' +'(' + str(incident_angle) + ', '+str(chushetianding)+', '+str(chushefangwei) + ')' + '.xls')
data_new = data_file[['Center Value', 'Reflective angle']]
print(data_new.head())
plt.plot(data_new['Reflective angle'], data_new['Center Value'], 'bo-',label=u"BRDF Curve",linewidth=1)
plt.title('Incident angle = ' + str(incident_angle) + 'degree')
plt.legend()

plt.xlabel(u"Azimuth Viewing Angle")
plt.ylabel(u"Pixel Value")
plt.savefig('(' + str(incident_angle) + ', '+str(chushetianding)+', '+str(chushefangwei)+')'+'.png')