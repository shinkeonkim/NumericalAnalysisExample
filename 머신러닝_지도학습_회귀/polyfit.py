# polyfit 메소드를 통한 다항 회귀
# in order to how to use polyfit mothod in numpy 
import numpy as np
import matplotlib.pyplot as plt

# data 설정
x=np.array([0,1,2,3,4,5])
y=np.array([0, 0.8, 0.9, 0.1, -0.8, -1])
n=np.size(x)

# 수식으로 도출된, 기울기와 y절편
# (편미분을 활용한 식, np.polyfit과 동일한 역할이다.)
b=(n*np.sum(x*y)-(np.sum(x)*np.sum(y)))/(n*np.sum(x**2)-(np.sum(x))**2)
# b= -0.30285714285714288: slope
a=(np.sum(y)-b*np.sum(x))/n
# 0.75714285714285723: intercept

# numpy의 polyfit 함수
p1=np.polyfit(x,y,1)  
print(p1)
# 결과 -> [-0.30285714,  0.75714286]
# 이 값의은 p1 이 -0.30285714 * x + 0.75714286 의 직선을 의미한다는 것이다.
# 따라서, p1의 첫번째 값은 기울기 slope, 두번째 값은  y절편 intercept를 의미한다.
plt.figure(1)
plt.plot(x, y, 'o')
plt.grid()
plt.plot(x, np.polyval(p1,x), 'r-')  # p1 from np.polyfit, plot(x, p1 with polyval

# 사실상 위와 동일한 내용임
# 왜냐하면, np.polyval이 첫번째 인자인 식에 x를 대입한 값을 return하기 때문에.
plt.figure(2)
plt.plot(x, y, 'o')
plt.grid()
plt.plot(x, p1[0]*x+p1[1], 'r-')

plt.show()