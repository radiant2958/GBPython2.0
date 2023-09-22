# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json 
import csv
import hashlib
import os
import pickle


def processe_file_to_json(numbers_file, names_file, json_file):
    with open(numbers_file, 'r') as num_file, open(names_file, 'r') as nam_file:
        numbers = num_file.readlines()
        names = nam_file.readlines()

        max_len = max(len(names), len(numbers))
        data = {}

        for i in range(max_len):
            int_num, float_num = map(float, numbers[i % len(numbers)].strip().split("|"))
            product = int_num * float_num

            if product < 0:
                output_name = names[i % len(names)].strip().capitalize()  
                data[output_name] = abs(product)
            else:
                output_name = names[i % len(names)].strip().capitalize()
                data[output_name] = round(product)

    with open(json_file, 'w') as jf:
        json.dump(data, jf, indent=4)  

# processe_file_to_json("test.txt", "name.txt", "result.json")


# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.


def add_user_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):  # Если файл не найден или пуст, создаем новый словарь
        data = {str(i): {} for i in range(1, 8)}  # Группировка по уровню доступа

    while True:
        # Запрашиваем данные пользователя
        name = input("Введите имя: ")
        user_id = input("Введите личный идентификатор: ")
        unique_id = False
        while not unique_id:
            for level in data.values():
                if user_id in level.keys():
                    print("Такой идентификатор уже существует. Пожалуйста, введите другой.")
                    user_id = input("Введите личный идентификатор: ")
                    
                else:
                    unique_id = True


        access_level = input("Введите уровень доступа (от 1 до 7): ")
        valid_access_level = False
        while not valid_access_level:
            if access_level.isdigit() and 1 <= int(access_level) <= 7:
                valid_access_level = True
            else:
                print("Уровень доступа должен быть числом от 1 до 7.")
                access_level = input("Введите уровень доступа (от 1 до 7): ")

        data[access_level][user_id] = name

     
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

       
        cont = input("Хотите добавить еще одного пользователя? (yes/no): ")
        if cont.lower() != 'yes':
            break

# add_user_data("users.json")


# Задание №3
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as js_file:
        data = json.load(js_file)

    with open(csv_file, 'w', newline='') as c_f:
        writer = csv.writer(c_f)

        writer.writerow(['Level', 'User id', 'Name'])

        for level, user in data.items():
            for user_id, name in user.items():
                writer.writerow([level, user_id, name])

    print(f'Фаил сохранен {csv_file}')

# json_to_csv('users.json', 'users.csv')

# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

def from_csv_to_json(input_csv, output_json):
    data = []

    with open(input_csv, 'r') as csv_file:
        reader = csv.reader(csv_file)

        next(reader)

        for row in reader:
            level, user_id, name = row

            user_id = user_id.zfill(10)

            name = name.capitalize()

            hash_id = hashlib.sha256()
            hash_id.update((name + user_id).encode('utf-8'))
            hash_value = hash_id.hexdigest()

            data.append({"Level": level, "User Id": user_id, "Name": name, "Hash_id": hash_value})

    with open(output_json, 'w') as json_file:
        json.dump(data,json_file, indent=1)


# from_csv_to_json('users.csv','from_csv_to.json')            


# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

def json_to_pickle(directory):

    files = os.listdir(directory)
    json_files = [f for f in files if f.endswith('.json')]


    for i in json_files:
        with open(os.path.join(directory, i), 'r') as json_file:
            data = json.load(json_file)

        pfile = i[:-5] + '.pickle'
        with open(os.path.join(directory,pfile), 'wb') as pickle_file:
            pickle.dump(data, pickle_file) 


# json_to_pickle("/Users/radiant5/Desktop/GBPython2.0")


# Задание №6
# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

def pickle_to_csv(pickle_file, csv_file):
    with open(pickle_file, 'rb') as pf:
        data = pickle.load(pf)


    if not data:
        print('файл пустой')
        return
    
    headers = data[0].keys()

    with open(csv_file, 'w', newline='') as cf:
        writer = csv.DictWriter(cf, headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


# pickle_to_csv('from_csv_to.pickle', 'pickle_to_csv.csv')


# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

def csv_to_pickle_str(csv_file):
    data = []

    with open(csv_file, 'r') as cf:
        reader = csv.reader(cf)
        heanders = next(reader)
        for row in reader:
            entry = {heanders[i]: value for i,value in enumerate(row)}
            data.append(entry)
    
    pickled_data = pickle.dumps(data)
    return pickled_data


pickle_string = csv_to_pickle_str('users.csv')
print(pickle_string)