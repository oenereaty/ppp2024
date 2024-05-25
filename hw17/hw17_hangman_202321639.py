import random
import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()
window.title("hangman game")


def gui_input(text):
    return simpledialog.askstring(title="Test", prompt=text)


def select_subject():
    print("어떤 주제의 단어를 고르시겠습니까?")
    subject = gui_input("1.과일\n2.스포츠\n3.나라 이름\n")

    menu = {"1": "과일.txt", "2": "스포츠.txt", "3": "나라 이름.txt"}

    if subject in menu.keys():
        with open(menu[subject], encoding='UTF-8') as f:
            line = f.readline()

        lists = []
        tokens = line.split(",")
        for token in tokens:
            lists.append(token)

        juje = (menu[subject]).strip(".txt")
        print(f"주제는 {juje}입니다")
    else:
        print("프로그램을 종료합니다.")
        return None
    return line


def text2list(line):
    words = []
    tokens = line.split(",")
    for token in tokens:
        words.append(token.strip())
    return words


def choice(words):
    hidden_answer = random.choice(words)
    return hidden_answer


def update_shown_answer(shown_answer, hidden_answer, x):
    result = []

    for shown_text, hidden_text in zip(shown_answer, hidden_answer):
        if shown_text == "_":
            if x == hidden_text:
                result.append(x)
            else:
                result.append("_")
        else:
            result.append(shown_text)

    return "".join(result)


def main():
    lines = select_subject()

    input_text = text2list(lines)
    hidden_answer = random.choice(input_text)
    problem = ["_" for _ in range(len(hidden_answer))]
    shown_answer = "".join(problem)
    trial = 5

    while True:
        print(f"{shown_answer}, 생명 개수: {trial}")
        x = gui_input("알파벳을 입력하세요:")

        if x in hidden_answer:
            shown_answer = update_shown_answer(shown_answer, hidden_answer, x)
        else:
            trial -= 1
            if trial <= 0:
                print(f"정답을 맞추지 못 했습니다. 정답은 {hidden_answer}입니다.")
                break

        if "_" not in shown_answer:
            print("축하합니다. 정답입니다~~~~~~~~~")
            break


if __name__ == "__main__":
    main()
