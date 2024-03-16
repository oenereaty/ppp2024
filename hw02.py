#1
print("°C->°F, K으로 변환하기")
c1 = float(30)
k =  float(c1 + 273.15)
f =  float((9/5)*c1+32)
print("{}°C는 {}°F, {}K입니다.".format(c1,f,k))


#2
c2 =  float(0)
k =  float(c2 + 273.15)
f =  float((9/5)*c2+32)
print("{}°C는 {}°F, {}K입니다.\n".format(c2,f,k))


#3
print("BMI 계산하기")
weight =  int(60)
height =  int(170)
m = height*0.01
BMI = float(weight/m**2)
print("{}cm, {}kg인 사람의 BMI 지수는 {}입니다.\n".format(height, weight, BMI))


#4
print("원 면적 구하기")
r =  int(4)
import math
math.pi
S = (r**2) * (math.pi)
print("반지름이 {}인 원의 면적은 {}입니다.\n".format(r,S))


#5
print("사다리꼴 면적 구하기")
long =  int(5)
short =  int(3)
h =  int(4)
S = (long + short) * h * (1/2)
print("윗변이{}, 밑변이 {}, 높이가 {}인 사다리꼴의 면적은 {}입니다.".format(short, long, h,S))
 
