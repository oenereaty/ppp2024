def average(nums):

    count = 0
    for num in nums:
        if num != 0:
            count += 1


    return sum(nums) / count
    

    
def median(nums):

    sorting = sorted(nums)
    length = len(sorting)


    if length % 2 == 0:
        mid = sorting[(length // 2)] # 인덱스는 0부터 시작함

    else: 
       mid = sorting[((length-1) // 2)]


    return mid



def text2list(input_text):
    
    tokens = input_text.split()
    nums = []
    
    for token in tokens:
        nums.append(int(token))


    return nums



def read_file_multi_line(filename):
    data = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            text = line.strip().split()
            for num in text:
                value = int(num)
                data.append(value)
            
    return data



#==============외부 파일에서 자료 불러오기==============


def main():
    textfile = r"C:\Users\user\Desktop\ppp_0403\number3.txt"
    
    nums = read_file_multi_line(textfile)
    ave = average(nums)
    med = median(nums)
    sorting = sorted(nums)
    the_number = len(nums)

    print("주어진 리스트는", nums, "입니다.")
    print(f"주어진 리스트의 오름차순입니다:{sorting}")
    print(f"주어진 리스트의 숫자 개수는 {the_number}입니다.")
    print(f"주어진 리스트의 평균값은 {ave:.1f}입니다.")
    print(f"주어진 리스트의 중앙값은 {med}입니다.")
    print("주어진 리스트의 최솟값은", min(nums), "입니다.")
    print("주어진 리스트의 최댓값은", max(nums), "입니다.")


if __name__ == "__main__":
    main()