import os
import sys
import requests
import matplotlib.pyplot as plt
import numpy as np

if "./" not in sys.path:
    sys.path.append("./")


def download(filename, URL):
    if not os.path.exists(filename):
        res = requests.get(URL)
        with open(filename, "w", encoding="UTF-8") as f:
            f.write(res.text.replace("\r", ""))


def read_dates(filename):
    dataset = []
    with open(filename, encoding='UTF-8') as f:
        lines = f.readlines()

        for line in lines[8:]:
            tokens = line.split(",")
            year = int(tokens[0])
            month = int(tokens[1])
            day = int(tokens[2])
            dataset.append((year, month, day))

    return dataset


def read_col(filename, col_name):
    dataset = []
    with open(filename, encoding="UTF-8") as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[0].split(",")]
        col_idx = header.index(col_name)

        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[col_idx]) if tokens[col_idx] else np.nan)

    return dataset

def read_col_int(filename, col_name):
    dataset = []
    with open(filename, encoding="UTF-8") as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[0].split(",")]
        col_idx = header.index(col_name)

        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(int(tokens[col_idx]) if tokens[col_idx] else np.nan)

    return dataset


def tagv_summer_winter(dataset, tavg):
    summer = []
    winter = []
    for (year, month, day), temp in zip(dataset, tavg):
        if month == 7:
            summer.append(temp)
        elif month == 1:
            winter.append(temp)
    return summer, winter

def birthday_temp(dataset, month, day):
    birthdays = []
    for record in dataset:
        record_year, record_month, record_day = record
        if record_month == month and record_day == day:
            birthdays.append(record)
    return birthdays


def main():
    URL = "https://api.taegon.kr/stations/146/?sy=1980&ey=2023&format=csv"
    filename = "jeonju_all.csv"
    download(filename, URL)

    dataset = read_dates(filename)
    tavg = read_col(filename, "tavg")
    years = read_col_int(filename, "year")
    years_list = list(set(years))


    birthday_data = birthday_temp(dataset, 2, 8)
    summer, winter = tagv_summer_winter(dataset, tavg)

    plt.figure(figsize=(15, 6))
    plt.plot(summer, color="r", label="여름온도")
    plt.plot(winter, color="b", label="겨울온도")

    plt.ylabel("Temperature(℃)")
    plt.xlabel("Year")
    plt.legend()

    plt.rcParams['font.family'] = ['Gulim', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False

    plt.savefig("./line_temp.png")
    plt.show()


if __name__ == "__main__":
    main()