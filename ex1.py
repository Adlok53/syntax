# Приветсвие
print("Добро пожаловать на поисковик")

# Пример данных
list = [
    {"text": "test", "created_date": "1", "rubrics": "example"}
]

# Загрузка данными
text = input("Введите заголовок ")
created_date = input("Введите дату ")
rubrics = input("Введите рубрику ")

# Сохранение данных
add = {"text": text, "created_date": created_date, "rubrics": rubrics}

# Добавление введеных данных
list.append(add)

# Вывод результата
print(list)