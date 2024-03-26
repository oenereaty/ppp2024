def gugudan(dan):
   
   for i in range(9):
        print(f"{dan} * {i+1} = {dan * (i+1)}")

   


def main():
    dan = int(input("몇 단을 입력할까요?:"))
    gugudan(dan)


if __name__ == "__main__":
    main()


        