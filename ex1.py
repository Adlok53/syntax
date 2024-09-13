print("Добро пожаловать на поисковик")

list = [
    {"text": "test", "created_date": "1", "rubrics": "example"}
]

text = input("Введите заголовок ")
created_date = input("Введите дату ")
rubrics = input("Введите рубрику ")

add = {"text": text, "created_date": created_date, "rubrics": rubrics}

list.append(add)

print(list)