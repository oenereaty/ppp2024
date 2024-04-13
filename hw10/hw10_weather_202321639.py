

# def read_tmax(filename):
#     result1 = []
#     with open(filename) as f:
#         lines = f.readlines()
#         for line in lines[1:]:
#             tokens = line.split(",")
#             tmax = float(tokens[3])
#             result1.append(tmax)

#     return result1


# def read_tmin(filename):
#     result2 = []
#     with open(filename) as f:
#         lines = f.readlines()
#         for line in lines[1:]:
#             tokens = line.split(",")
#             tmin = float(tokens[5])
#             result2.append(tmin)

#     return result2



def read_tavg(filename):
    result3 = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            tavg = float(tokens[4])
            result3.append(tavg)

    num_result3 = len(list(result3))
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
    tavg = read_tavg("weather(146)_2022-2022.csv")
    total_rain = total_rainfall("weather(146)_2022-2022.csv")
    rainfall_5mm = rainfall("weather(146)_2022-2022.csv")
    
    print(f"연 평균 기온은 {(tavg):.1f}°C입니다.")
    print(f"5mm 이상 강우일수는 {rainfall_5mm}일입니다.")
    print(f"총 강우량은 {total_rain}mm입니다")

 




    
    
    

if __name__ == "__main__":
    main()