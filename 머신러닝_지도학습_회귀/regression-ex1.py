import numpy as np
import matplotlib.pyplot as plt

# polyfit.py에서 사용한 데이터셋
x=np.array([0,1,2,3,4,5])
y=np.array([0, 0.8, 0.9, 0.1, -0.8, -1])
n=np.size(x)

# 수식으로 도출된 기울기와 y절편
b=(n*np.sum(x*y)-(np.sum(x)*np.sum(y)))/(n*np.sum(x**2)-(np.sum(x))**2)
a=(np.sum(y)-b*np.sum(x))/n
# b= -0.30285714285714288
# a= 0.75714285714285723

fx=b*x+a
# print(fx) -> [ 0.75714286  0.45428571  0.15142857 -0.15142857 -0.45428571 -0.75714286]

# 이 예시로 보았을 때, 3번째 인자가, 몇개의 항을 사용할지 나타낸다는 것을 알 수 있음.
# 예를 들어, p1은 p1[0] * x + p1[1] 라는 수식에서 계수들을 나타내고,
p1=np.polyfit(x, y, 1)
# p1=array([-0.30285714,  0.75714286])

# p2는 p2[0] * x * x + p2[1] * x + p2[2]라는 수식에서 계수들을 나타내고,
p2=np.polyfit(x, y, 2)

# p3는 p3[0] * x * x * x+ p3[1] * x * x + p3[2] *x + p3[3] 라는 수식에서 계수 나타낸다는 것이다.
# array([-0.16071429,  0.50071429,  0.22142857])
p3=np.polyfit(x, y, 3)
# array([ 0.08703704, -0.81349206,  1.69312169, -0.03968254])


# 그럼, 출력을 해보자.
# 1번째 figure에는 
plt.figure(1)
# x와 y에 있는 값들로 점을 찍고,
plt.plot(x,y, 'o')
# 수식으로 구한 fx를 빨간 수식으로 출력해본다.
plt.plot(x,fx, 'r*-')

# 2번째 figure에는
plt.figure(2)
# 앞서 마찬기지로, x와 y에 있는 값들로 점을 찍고,
plt.plot(x,y, 'o')
# p1을 활용한 수식으로 출력해본다.(사실상 figure 1과 동일한 결과이다. 조금의 값 차이는 있다.)
plt.plot(x, np.polyval(p1, x), 'b*-')
# = plt.plot(x,fx, 'r*-')

# 3번째 figure에는
plt.figure(3)
# 또 x와 y에 있는 값들로 점을 찍고
plt.plot(x,y, 'o')
# p1, p2, p3를 활용해 출력해본다.
# p1은 일차함수(직선), p2는 이차 함수, p3는 삼차함수이다.
plt.plot(x, np.polyval(p1,x), 'r*-')
plt.plot(x, np.polyval(p2,x), 'b>-')
plt.plot(x, np.polyval(p3,x), 'mx-')

# 4번째 figure에는 
plt.figure(4)
# 또또, x와 y에 있는 값들로 점을 찍고
plt.plot(x, y, 'o')
# 그리드도 표시하고,
plt.grid()

# -2~ 6까지 100개의 값으로 선형 간격의 배열을 만든뒤,
xp=np.linspace(-2, 6, 100)
# 이 값으로 점들을 x값이라 생각하고 각각 p1, p2, p3에 대입한 점들을 이어 곡선으로 그린다.
# 앞서 그린 그래프들보다, 간격도 좁고, 점이 많아서 더 자연스럽게 보인다.
plt.plot(xp, np.polyval(p1,xp), 'r-') 
plt.plot(xp, np.polyval(p2,xp), 'b--') # --: dached line
plt.plot(xp, np.polyval(p3,xp), 'm:')

# 출력
plt.show()