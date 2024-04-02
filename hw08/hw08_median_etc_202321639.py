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
    
    tokens = input_text.split(",")
    nums = []
    
    for token in tokens:
        nums.append(int(token))


    return nums



def main():
    input_text = input("숫자를 콤마를 이용해 작성하세요:")
    
    nums = text2list(input_text)
    ave = average(nums)
    med = median(nums)

    print("주어진 리스트는",(nums),"입니다.")

    print("주어진 리스트의 평균값은 {:.1f}입니다.".format(average(nums)))

    print("주어진 리스트의 중앙값은 {}입니다.".format(median(nums)))

    print("주어진 리스트의 최솟값은",min(nums),"입니다.")

    print("주어진 리스트의 최댓값은",max(nums),"입니다.")


    
if __name__ == "__main__":
    main()