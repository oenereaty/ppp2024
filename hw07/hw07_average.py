def average(nums):
    t = sum(nums) / 6
    return t



def main():
    x = [1, 3, 5, 90, 23, 48]
    average_num = average(x)



    print(f"평균값은 {average_num:.2f}입니다.")
if __name__ == "__main__":
    main()