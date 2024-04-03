print("BMI 계산하기")
weight =  int(60)
height =  int(170)
m = height*0.01
BMI = float(weight/m**2)
print("{}cm, {}kg인 사람의 BMI 지수는 {}입니다.\n".format(height, weight, BMI))