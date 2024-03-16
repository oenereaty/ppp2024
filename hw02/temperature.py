print("°C->°F, K으로 변환하기")
c1 = float(input("온도를 입력하시오. "))
k =  c1 + 273.15
f =  (9/5)*c1+32
print("{}°C는 {}°F, {}K입니다.\n".format(c1,f,k))