def total_calorie(fruits, fruits_calorie_dic):
    
    total_kcal = 0
    
    for fruits, ate_gram in fruits_calorie_dic.items():
        total_kcal += fruits_calorie_dic[fruits] * ate_gram

    return total_kcal

    

def main():
    
    fruits_cal_dic = {'딸기': 34, '한라봉': 50, '바나나': 77, '배': 46, '수박': 31}
    
    fruits={'딸기': 300, '한라봉': 150} #섭취량
    
    total_kcal = total_calorie(fruits, fruits_cal_dic)


    print(f"섭취한 칼로리수는 {total_kcal}입니다.")



if __name__ == "__main__":
    main()



