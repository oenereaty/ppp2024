#지난 hw04 중 사전형을 이용한 kcal 계산 파일이 착오로 인해 잘못 업로드 되었습니다.
#노파심에 정상 파일을 hw05에 업로드하였습니다.

print("섭취한 과일의 Kcal 구하기. 단, 먹지 않았을 경우 '0'을 입력하며, 정수로 입력하세요.")

str_g = int(input("섭취한 딸기(설향)의 무게(g)를 입력하세요:")) / 100
tan_g = int(input("섭취한 한라봉의 무게(g)를 입력하세요:")) / 100
ban_g = int(input("섭취한 바나나의 무게(g)를 입력하세요:")) / 100
pear_g = int(input("섭취한 배의 무게(g)를 입력하세요:")) / 100
wat_g = int(input("섭취한 수박의 무게(g)를 입력하세요:")) / 100

kcal = {'딸기': 34, '한라봉': 50, '바나나': 77, '배': 46, '수박': 31}

total_kcal = 0
i = 0

if str_g != 0:
    total_kcal += kcal['딸기'] * str_g
    i += 1
if tan_g != 0:
    total_kcal += kcal['한라봉'] * tan_g
    i += 1
if ban_g != 0:
    total_kcal += kcal['바나나'] * ban_g
    i += 1
if pear_g != 0:
    total_kcal += kcal['배'] * pear_g
    i += 1
if wat_g != 0:
    total_kcal += kcal['수박'] * wat_g
    i += 1

print(f"먹은 과일의 개수는 {i}종류이며, 총 {total_kcal:.2f}kcal를 섭취했습니다.")
