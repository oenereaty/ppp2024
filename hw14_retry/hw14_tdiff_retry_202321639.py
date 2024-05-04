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

        for line in lines[8:]:
            tokens = line.split(",")
            date = tokens[0]
            year = date.split("-")[0]
            month = date.split("-")[1]
            day = date.split("-")[2]
            dates = (year, month, day)
            dataset.append(dates)
    # print(dataset)

    return dataset





def read_col(filename, col_name):
    dataset = []
    with open(filename, encoding="UTF-8") as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[7].split(",")]
        col_idx = header.index(col_name)
        # print(col_idx)
        for line in lines[8:]:
            tokens = line.strip().split(",")
            # print(tokens)
            if tokens[col_idx] != '':
                dataset.append(float(tokens[col_idx]))
            else:
                dataset.append("웅")
        # print(dataset)
        # print(type(tokens[col_idx]))
    return dataset





def temp_max(tmax):
    numbers = []
    for item in tmax:
        if item != '웅':
            numbers.append(item)
        else:
            continue
    #print(type(numbers))

    find_tmax = max(numbers)
    #print(find_tmax)

    max_idx1 = tmax.index(find_tmax)
   # print(max_idx1)
    return find_tmax, max_idx1




def find_temp_diff(tmax, tmin):
    temp_diffrent = []
    for idx, (tx, tn) in enumerate(zip(tmax, tmin)):
        if tx != '웅' and tn != '웅':
            temp_diff = float(tx) - float(tn)
            temp_diffrent.append((temp_diff, idx))

    max_diff, max_idx2 = max(temp_diffrent)
    # print(max_diff, max_idx2)
    return max_diff, max_idx2






def main():
    URL = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=1904&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="
    filename = "jeonju_all.csv"
    download(filename, URL)
    tmax = read_col(filename, "최고기온(℃)")
    tmin = read_col(filename, "최저기온(℃)")
    find_tmax, max_idx1 = temp_max(tmax)
    find_diff_max, max_idx2 = find_temp_diff(tmax, tmin)
    find_date = read_dates(filename, max_idx1)
    find_date2 = read_dates(filename, max_idx2)
    # print("test")




    hw_submission.submit('채경원', find_tmax, read_dates(filename, max_idx1)[max_idx1], find_diff_max, read_dates(filename, max_idx2)[max_idx2])
    # hw_submission.submit('채경원', find_tmax, read_dates(filename, max_idx1, find_diff_max, read_dates(filename, max_idx2)))
    # hw_submission.submit('채경원', tmax, read_dates(filename, max_idx1, temp_diff_max, read_dates(filename, max_idx2)))

if __name__ == "__main__":
    main()