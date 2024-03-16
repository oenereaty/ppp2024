print("BMI 계산하기")
weight =  float(input("몸무게를 입력하시오. "))
height =  float(input("키를 입력하시오. "))
m = height*0.01
BMI = float(weight/m**2)
print("{}cm, {}kg인 사람의 BMI 지수는 {}입니다.\n".format(height, weight, BMI))