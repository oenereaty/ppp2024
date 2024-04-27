


def read_tavg(filename):
    result3 = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            tavg = float(tokens[4])
            result3.append(tavg)

    num_result3 = len(result3)
    sum_result3 = float(sum(result3))    
    tavg = sum_result3 / num_result3


    return tavg



def rainfall(filename):
    result4 = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            rainfall = float(tokens[9])
            result4.append(rainfall)


        num = 0
        for rainfall in result4:
            if rainfall >= 5:
                num += 1


    return num


def total_rainfall(filename):
    result5 = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            rainfall2 = float(tokens[9])
            result5.append(rainfall2)

        total_rain = (sum(result5))

    return total_rain   



def main():
    import requests
    import os



    URL = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
    filename = "weather(146)_2020-2020.csv"




    if not os.path.exists(filename):
        res = requests.get(URL)
        with open(filename, "w", encoding="UTF-8") as f:
            f.write(res.text)




    tavg = read_tavg(filename)
    total_rain = total_rainfall(filename)
    rainfall_5mm = rainfall(filename)



    with open("hw13.txt", "w", encoding="UTF-8") as f:
        f.write(f"연 평균 기온은 {(tavg):.1f} °C \n")
        f.write(f"총 강우량은 {str(total_rain)}mm \n")
        f.write(f"5mm 이상 강우일수는 {str(rainfall_5mm)}일\n")




if __name__ == "__main__":
    main()