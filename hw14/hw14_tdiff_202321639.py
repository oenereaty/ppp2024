import os
import sys
import requests
import hw_submission


if "./" not in sys.path:
    sys.path.append("./")

def download(filename, URL):
    if not os.path.exists(filename):
        res = requests.get(URL)
        with open(filename, "w", encoding="UTF-8") as f:
            # f.write(res.text)
            f.write(res.text.replace("\r", ""))


def read_dates(filename, col_name):
    dataset = []
    with open(filename, encoding='UTF-8') as f:
        lines = f.readlines()

        # print(col_idx)
        for line in lines[8:]:
            tokens = line.split(",")
            date = tokens[col_name]
            # print(date)
            year = date.split("-")[0]
            month = date.split("-")[1]
            day = date.split("-")[2]
            dates = (year, month, day)
            dataset.append(dates)

    return dataset



def read_col(filename, col_name):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[3].split(",")]
        col_idx = header.index(col_name)
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[col_idx]))
    return dataset



def temp_max(temperatures):
    tmax = max(temperatures)
    max_idx1 = temperatures.index(tmax)
    return tmax, max_idx1

def temp_diff_max(tmax, tmin):
    temp_diff = [tx - tn for tx, tn in zip(tmax, tmin)]
    max_diff = max(temp_diff)
    max_idx2 = temp_diff.index(max_diff)
    return max_diff, max_idx2



def main():
    URL = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=1904&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="
    filename = "jeoju_all.csv"
    tmin = read_col(filename, [3])
    download(filename, URL)
    tmax, max_idx1 = temp_max(filename)
    tdiff_max, max_idx2 = temp_diff_max(tmax, tmin)


    hw_submission.submit('채경원', tmax, read_dates(filename, max_idx1), temp_diff_max, read_dates(filename, max_idx2))
    # hw_submission.submit('채경원', tmax, dates[max_idx1], temp_diff_max, dates[max_idx])
    # hw_submission.submit("채경원", 340.1, "2011-08-04", 25.2, "1978-01-04")

if __name__ == "__main__":
    main()