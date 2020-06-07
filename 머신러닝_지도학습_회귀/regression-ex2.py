import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10, 90, 10.)
y = np.array([25, 70, 380, 550, 610, 1220, 830, 1450])
plt.figure(10)
plt.plot(x, y, 'ro-')
plt.grid()

xsum=np.sum(x)
ysum=np.sum(y)
# 360.0
# 5135
xysum=sum(x*y)
n=np.size(x)
xavg=xsum/n # 45.0
yavg=ysum/n # 641.875
a1=(n*xysum-xsum*ysum)/(n*sum(x**2)-xsum**2)
# 19.470238095238095
a0= yavg-xavg*a1
# -234.28571428571422
y1=a1*x+a0
#array([-39.58333333, 155.11904762, 349.82142857, 544.52380952,
# 739.22619048, 933.92857143, 1128.63095238, 1323.33333333])
plt.figure(11)
plt.plot(x, y, 'ro-', x, y1, 'b*-')
plt.grid()
plt.show()