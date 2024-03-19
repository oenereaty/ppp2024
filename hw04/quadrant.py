print("두 지점 사이 거리 구하기. 단, 좌표는 정수로 입력하세요.")
x = int(input("x좌표를 입력해주세요:"))
y = int(input("y좌표를 입력해주세요:"))


if x>0 and y>0:
    print("입력하신 ({},{})은(는) 1사분면입니다.".format(x,y))
elif x<0 and y>0:
    print("입력하신 ({},{})은(는) 2사분면입니다.".format(x,y))
elif x<0 and y<0:
    print("입력하신 ({},{})은(는) 3사분면입니다.".format(x,y))
elif x>0 and y<0:
    print("입력하신 ({},{})은(는) 4사분면입니다.".format(x,y))
else:
    print("입력하신 ({},{})은(는) 원점입니다.".format(x,y))