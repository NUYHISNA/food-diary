import datetime
import json


FILE_NAME = "meal_record.json"

def file_read():
    with open(FILE_NAME, "r", encoding='UTF-8')as f:
        data = json.load(f)
    return data

def get_data_from_user(data):
    date = datetime.datetime.now()
    date_key = date.strftime("%Y_%m_%d")

    data[date_key] = {"아침": [], "점심": [], "저녁": []}

    breakfast = input("아침: ")
    data[date_key]["아침"] = breakfast.split()

    lunch = input("점심: ")
    data[date_key]["점심"] = lunch.split() 

    dinner = input("저녁: ")
    data[date_key]["저녁"] = dinner.split()
    return data

def file_write(user_data):
    with open(FILE_NAME, "w", encoding='UTF-8') as f:
        json.dump(user_data, f, indent=4, ensure_ascii=False)


print("==== end recording the meal ====")
get_data = file_read()
food = get_data_from_user(get_data)
result = file_write(food)
print("==== end recording the meal ====")