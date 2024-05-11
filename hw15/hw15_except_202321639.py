
def str2int(datas):
    int_datas = []
    for i in datas:
        try:
            int_data = int(i)
        except ValueError:
            print(f"'{i}'는 정수로 변환할 수 없습니다")
        else:
            int_datas.append(int_data)
    return int_datas


def num_avg(int_datas):
    len_datas = len(int_datas)
    sum_datas = sum(int_datas)
    return sum_datas / len_datas, len_datas


def main():
    datas = []
    # data = input("데이터를 입력하세요. -1을 입력하면 입력을 받지 않습니다.")

    while True:
        data = input("데이터를 입력하세요. -1을 입력하면 입력을 받지 않습니다.")
        datas.append(data)

        if data == '-1':
            del datas[-1]
            break

    print(f"입력받은 값은 {datas}입니다.")


    int_datas = str2int(datas)
    leng = num_avg(int_datas)[1]
    avg = num_avg(int_datas)[0]

    print(f"총 {leng:.0f}개의 자연수가 입력되었고, 평균은 {avg:.0f}입니다.")





if __name__ == "__main__":
    main()