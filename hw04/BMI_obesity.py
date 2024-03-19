print("BMI calculator")
weight =  float(input("몸무게를 입력하세요:"))
height =  float(input("키를 입력하세요:"))
m = height*0.01
BMI = float(weight/m**2)


lose_weight = (BMI - 22.9) * (m**2)



if BMI<23:
    print("키가 {}cm이고, 몸무게가 {}kg인 사람은 BMI지수가 {:.1f}이므로, 정상입니다.".format(height,weight,BMI))

elif 23<=BMI<24.9:
    print("키가 {}cm이고, 몸무게가 {}kg인 사람은 BMI지수가 {:.1f}이므로, 비만 전단계입니다.약 {:.1f}kg을 감량하세요!".format(height,weight,BMI,lose_weight))

elif 25<=BMI<30:
    print("키가 {}cm이고, 몸무게가 {}kg인 사람은 BMI지수가 {:.1f}이므로, 1단계 비만입니다.약 {:.1f}kg을 감량하세요!".format(height,weight,BMI,lose_weight))

elif 30<=BMI<34.9:
    print("키가 {}cm이고, 몸무게가 {}kg인 사람은 BMI지수가 {:.1f}이므로, 2단계 비만입니다.약 {:.1f}kg을 감량하세요!".format(height,weight,BMI,lose_weight))

else:
    print("키가 {}cm이고, 몸무게가 {}kg인 사람은 BMI지수가 {:.1f}이므로, 3단계 비만입니다.약 {:.1f}kg을 감량하세요!".format(height,weight,BMI,lose_weight))
