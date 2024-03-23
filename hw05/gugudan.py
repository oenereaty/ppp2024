print("곱셈표를 표현하는 프로그램입니다.")
a = int(input("몇 단을 입력할까요?:"))
b = int(input("어디까지 곱할까요?:"))

for i in range(b):
    print(f"{a} * {i+1} = {a * (i+1)}")
    