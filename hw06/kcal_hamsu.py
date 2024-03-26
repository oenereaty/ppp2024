def kcal_calculator(total_kcal, eat_fruit):

    


    # fruits = {'딸기', '한라봉', '바나나', '배', '수박'}
    kcal = {'딸기': 34, '한라봉': 50, '바나나': 77, '배': 46, '수박': 31}
    total_kcal = 0
    i = 0


    for eat_fruit, eat_g in kcal.items():
            eat_g = int(input(f"섭취한 {eat_fruit}의 무게를 입력하세요:"))
            if eat_g != 0:
                i+=1
                total_kcal += kcal[eat_fruit] * (eat_g / 100) 


    return eat_fruit, eat_g, i, total_kcal

def main():

   


    print("섭취한 과일의 Kcal 구하기. 단, 먹지 않았을 경우 '0'을 입력하며, 정수로 입력하세요.")

    print(f"먹은 과일은 {i}종류이며, 총 {total_kcal:.2f}Kcal를 섭취하였습니다.")




if __name__ == "__main__":
    main()