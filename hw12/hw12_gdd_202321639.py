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

def gdd_season(tavg):
    total_gdd = 0
    for temp in tavg:
        if temp > 5:
            eff_temp = temp - 5
            total_gdd += eff_temp
    return total_gdd


def every_year_gdd(tavg, years, year):
    dataset = []
    for gdd, years in zip(tavg, years):
        if year == years:
            dataset.append(gdd)
    return dataset



def main():
    filename = "weather(146)_2001-2022.csv"
    tavg = read_col(filename, "tavg")
    years = read_col(filename, "year")
    
    for year in range(2001, 2023):
        yearly_gdd = every_year_gdd(tavg, years, year)
        print(f"{year}년의 gdd는 {gdd_season(yearly_gdd):.1f}")

if __name__ == "__main__":
    main()
