def total_calorie(fruits_eat, fruits_cal_dic):

    total = 0
    for fruit_name, fruit_gram in fruits_eat.items():
        total += fruit_gram * fruits_cal_dic[fruit_name] / 100
    return total

   


def main():
    fruits_calorie_dic = read_cal_db(r"C:\Users\qnsgh\OneDrive\바탕 화면\hw10\calorie_db.csv")



    fruits_mon = {"딸기": 300, "귤": 150, "쑥": 150, "고구마": 200, "칼슘나무 열매": 150}

    print("섭취한 칼로리는",total_calorie(fruits_mon, fruits_calorie_dic),"Kcal입니다.")
    print("섭취한 것은",list(fruits_mon.keys()),"입니다.")
    
    



def read_cal_db(filename):
    database = {}
    with open(filename, encoding = "utf-8-sig") as f:
        lines = f.readlines()
        
        
        for line in lines[1:]:
            tokens = line.split(",")
            fruit_name = tokens[0]
            fruit_cal = int(tokens[1])
            database[fruit_name] = fruit_cal
            
    return database
    
    
    
    

if __name__ == "__main__":
    main()
