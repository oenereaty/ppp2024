import random
import tkinter as tk
from tkinter import simpledialog
window = tk.Tk()
window.withdraw()


def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)

def select_subject():
    print("어떤 주제의 단어를 고르시겠습니까?")
    subject = gui_input("1.과일 및 채소\n2.동물\n3.국가\n")

    menu = {"1": "과일 및 채소.txt", "2": "동물.txt", "3": "국가.txt"}

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


def get_chosung(hidden_answer):
    chosung_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ',
                    'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    chosung = []

    for geulja in hidden_answer:
        chosung_idx = (ord(geulja) - ord('가')) // 588

        chosung.append(chosung_list[chosung_idx])
    return chosung


def main():
    lines = select_subject()
    words = text2list(lines)
    hidden_answer = choice(words)
    problem = get_chosung(hidden_answer)
    trial = 3
    shown_problem = "".join(problem)

    while True:
        print(f"주어진 초성은 '{shown_problem}'이며, 남은 생명은 {trial}개입니다.")
        x = gui_input("정답을 입력하세요:")

        if x == hidden_answer:
            print("정답입니다!")
            break
        else:
            trial -= 1
            if trial <= 0:
                print(f"정답은 {hidden_answer}입니다!")
                break


if __name__ == "__main__":
    main()