def get_range_list(n):
    return list(range(1, n+1))


def main():
    print("1부터 n까지 리스트로 돌려주는 프로그램입니다.")
    a = int(input("n:"))

    result = get_range_list(a)

    print("{}".format(result))


if __name__ == "__main__":
    main()