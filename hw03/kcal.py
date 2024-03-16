print("섭취한 과일의 Kcal 구하기. 단, 먹지 않았을 경우 '0'을 입력하며 정수로 입력하세요.")

str_g = int(input("섭취한 딸기(설향)의 무게(g)를 입력하세요."))/100
tan_g = int(input("섭취한 한라봉의 무게(g)를 입력하세요."))/100
ban_g = int(input("섭취한 바나나의 무게(g)를 입력하세요."))/100
pear_g = int(input("섭취한 배의 무게(g)를 입력하세요."))/100
wat_g = int(input("섭취한 수박의 무게(g)를 입력하세요."))/100


#이하 숫자는 100그람 당 kcal 수
str = 34
tan = 50 
ban = 77 
pear = 46 
wat = 31


a = str * str_g
b = tan * tan_g
c = ban * ban_g
d = pear * pear_g
e = wat * wat_g


kcal = (a+b+c+d+e)

print("섭취한 kcal는 {}입니다.\n".format(kcal))