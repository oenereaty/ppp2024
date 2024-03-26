def c2f(temp_c):
    return temp_c * 1.8 + 32 


def main():
    temp_c = float(input("섭씨 온도를 입력하세요:"))
    print("섭씨{}도는 화씨{:.2f}도입니다.".format(temp_c, c2f(temp_c)))



if __name__ == "__main__":
    main()