def is_leap_year(y):
    if y % 4 != 0:
        return "평년"
    elif y % 4 == 0:
        if y % 100 == 0 :
            return "평년"
        else:
            return "윤년"
    


def main():
    print("윤년 판정 프로그램입니다.")

    year = int(input("연도를 입력하세요:"))
    
    result = is_leap_year(year)

    print(f"{year}년은 {result}입니다.")



if __name__ == "__main__":
    main()