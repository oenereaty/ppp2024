print("삼각형 그리기 프로그램입니다.")

character = input("어떤 걸로 그릴까요?:")
a = int(input("높이?:"))

for i in range(0, a):
    print((character * (2*i+1)).center(2*a + 1))



