import random
import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()


def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)


def gugudan(n):
    score = []
    for i in range(n):
        a = random.randint(2, 9)
        b = random.randint(1, 9)
        c = (a * b)
        x = int(gui_input(f"{a}*{b}의 정답:"))
        if x == c:
            score.append(x)
        else:
            continue
    return score


def main():
    n = int(gui_input("몇 문제 푸시겠습니까?:"))
    score = gugudan(n)
    print(f"{n}문제 중 {len(score)}개를 맞혔으므로 {round(100 * (len(score) / n))}점입니다.")


if __name__ == "__main__":
    main()
