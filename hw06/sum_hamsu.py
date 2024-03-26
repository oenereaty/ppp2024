def sum_n(n):
    return (1+n)*(n / 2)



def main():
    print("1부터 n까지의 합을 구하는 프로그램입니다.")
    n = int(input("n:"))
    print("1부터 {}까지의 합은 {}입니다.".format(n,sum_n(n)))




if __name__ == "__main__":
    main()

