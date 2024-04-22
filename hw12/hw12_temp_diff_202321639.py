def read_col(filename, col_name):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[0].split(",")]
        
        col_idx = header.index(col_name)
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[col_idx]))
    
    return dataset


def read_dates(filename, col_name):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[0].split(",")]
        
        col_idx = header.index(col_name)
        for line in lines[1:]:
            tokens = line.split(",")
            year = int(tokens[0])
            month = int(tokens[1])
            day = int(tokens[2])
            dataset.append((year, month, day))
    
    return dataset


def find_max_diff(tmax, tmin):
    temp_diff = [tx - tn for tx, tn in zip(tmax, tmin)]

    max_idx = temp_diff.index(max(temp_diff))

    return temp_diff, max_idx
  


def get_data_ifs(values, conditions, criteria):
    dataset = []
    for td, year in zip(values, conditions):
        if year == criteria:
            dataset.append(td)
    return dataset


def main():
    filename = "weather(146)_2001-2022.csv" 
    tmax = read_col(filename, "tmax")
    tmin = read_col(filename, "tmin")
    years = read_col(filename, "year")
    months = read_col(filename, "month")
    days = read_col(filename, "day")
    dates = read_dates(filename, "day")
    temp_diff, max_idx = find_max_diff(tmax, tmin)
    

    for year in range(2001, 2023):
        uak = get_data_ifs(temp_diff, years, year)
        print(f"{year}년의 일교차 데이터: {dates[max_idx]} {max(uak):.1f}")
        # ^^^^^^^연도와 해당 연도의 일교차 데이터는 작성하였으나 발생한 날짜는 출력하지 못 했습니다
        # max_idx를 연도마다 갱신하지 못하여 그런 것으로 추측하지만 확실하지는 않습니다
        # 이에 대하여 이슈를 남겨주시면 학습에 큰 도움이 될 것 같습니다!


if __name__ == "__main__":  
    main()
