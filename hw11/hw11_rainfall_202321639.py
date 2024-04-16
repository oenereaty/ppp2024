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

        total_rain = sum(result5)

    return total_rain


def longest_rainday(rainfall):
    rain_event = [0]  

    prev_rain_count = 0
    for rain in rainfall:
        if rain == 0:
            if prev_rain_count > 0:
                rain_event.append(prev_rain_count)
            prev_rain_count = 0
        else:
            prev_rain_count += 1

    return max(rain_event)


def largest_rainday(rainfall):
    rain_event = [0]  

    prev_rain = 0
    for rain in rainfall:
        if rain == 0:
            if prev_rain > 0:
                rain_event.append(prev_rain)
            prev_rain = 0
        else:
            prev_rain += rain 
    return max(rain_event)


def top_rank(values):
    values = read_col("weather(146)_2022-2022.csv", "tmax")
    return sorted(values, reverse = True)[:3]


def get_data_ifs(values, conditions, criteria):
    dataset = []
    for rain, year in zip(values, conditions):
        if year == criteria:
            dataset.append(rain)
    return dataset



def read_col(filename, col_name):
    dataset = []
    with open (filename) as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[0].split(",")]
        
        col_idx = header.index(col_name)
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[col_idx]))
    
    return dataset

def sumif_month(values, conditions, criteria):
    dataset = []
    for rain, month in zip(values, conditions):
        if month in criteria:
            dataset.append(rain)

    return dataset




def main():
    rainfall_data = read_col("weather(146)_2022-2022.csv", "rainfall")
    longest_rain = longest_rainday(rainfall_data)
    largest_rain = largest_rainday(rainfall_data)
    rainfall_all = read_col("weather(146)_2001-2022.csv", "rainfall")
    year_all = read_col("weather(146)_2001-2022.csv", "year")
    month = read_col("weather(146)_2022-2022.csv", "month")
    total_rainfall_2001 = get_data_ifs(rainfall_all, year_all, 2001)
    total_rainfall_2022 = get_data_ifs(rainfall_all, year_all, 2022)
    summer_rainfall_2022 = sumif_month(rainfall_data, month, [6, 7, 8])
    top = top_rank("weather(146)_2022-2022.csv")

    print(f"최장 연속 강우 일수는 {longest_rain}일입니다.")
    print(f"강우 이벤트 중 최대 강우량은 {largest_rain:.1f}mm입니다.")
    print(f"2001년의 총 강우량과 2022년의 총 강우량은 각각 {sum(total_rainfall_2001):.1f}mm, {sum(total_rainfall_2022):.1f}mm입니다.")
    print(f"여름철 강수량은 {sum(summer_rainfall_2022):.1f}mm 입니다.")
    print(f"가장 더운 날 TOP3는 {top}도입니다.")


if __name__ == "__main__":
    main()
