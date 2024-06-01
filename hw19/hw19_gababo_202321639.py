import tkinter as tk
from tkinter import messagebox
import random


def check_winner(player):
    select = ['주먹', '가위', '보자기']
    computer = random.choice(select)

    if player == computer:
        winner = "비겼습니다!"
    elif ((player == '주먹' and computer == '가위') or (player == '보자기' and computer == '주먹') or
          (player == '가위' and computer == '보자기')):
        winner = '당신이 이겼습니다!'
    else:
        winner = '컴퓨터가 이겼습니다!'

    messagebox.showinfo("결과", f"당신은 {player}, 컴퓨터는 {computer}이므로 {winner}")


def main():
    window = tk.Tk()
    window.title("가위 바위 보 게임")
    window.geometry("180x80")

    # 가위 버튼
    def click_rock():
        check_winner('주먹')

    rock_button = tk.Button(window, text="주먹", command=click_rock, width=5)
    rock_button.pack()

    # 바위 버튼
    def click_paper():
        check_winner('보자기')

    paper_button = tk.Button(window, text="보자기", command=click_paper, width=5)
    paper_button.pack()

    # 보 버튼
    def click_scissors():
        check_winner('가위')

    scissors_button = tk.Button(window, text="가위", command=click_scissors, width=5)
    scissors_button.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
