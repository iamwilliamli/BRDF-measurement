import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_file = pd.read_excel('/Users/William/brdfm/brightness data.xls')
data_new = data_file[['Center Value', 'Viewing Angle']]
plt.plot(data_new['Viewing Angle'], data_new['Center Value'], 'bo-',label=u"BRDF Curve",linewidth=1)
plt.title(u"Incident angle = 62.05 degree")
plt.legend()

plt.xlabel(u"Viewing Angle")
plt.ylabel(u"Pixel Value")
plt.savefig('brdf.png')