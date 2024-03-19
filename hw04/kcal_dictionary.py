print("섭취한 과일의 Kcal 구하기. 단, 먹지 않았을 경우 '0'을 입력하며, 정수로 입력하세요.")

str_g = int(input("섭취한 딸기(설향)의 무게(g)를 입력하세요:"))/100
tan_g = int(input("섭취한 한라봉의 무게(g)를 입력하세요:"))/100
ban_g = int(input("섭취한 바나나의 무게(g)를 입력하세요:"))/100
pear_g = int(input("섭취한 배의 무게(g)를 입력하세요:"))/100
wat_g = int(input("섭취한 수박의 무게(g)를 입력하세요:"))/100


g_list = [str_g, tan_g, ban_g, pear_g, wat_g]

#이하 숫자는 100그람 당 kcal 수
str = 34
tan = 50 
ban = 77 
pear = 46 
wat = 31

kcal = [34, 50, 77, 46, 31]

a = kcal[0] * str_g
b = kcal[1] * tan_g
c = kcal[2] * ban_g
d = kcal[3] * pear_g
e = kcal[4] * wat_g


i=0
if str_g !=0:
    i+=1
if tan_g !=0:
    i+=1
if ban_g !=0:
    i+=1
if pear_g !=0:
    i+=1
if wat_g !=0:
    i+=1
    

total_kcal = (a+b+c+d+e)

print("섭취한 과일은 {}종류이며, 총 kcal는 {:.1f}입니다.\n".format(i,total_kcal)) 