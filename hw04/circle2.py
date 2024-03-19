import math

print("원 면적 구하기")
r =  float(input("원의 반지름을 입력하세요:"))

L = 2 * r * (math.pi)
S = (r**2) * (math.pi)
print("반지름이 {}인 원의 둘레는 {:.1f}이고, 면적은 {:.2f}입니다.\n".format(r,L,S))