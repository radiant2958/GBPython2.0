
import random
import string
import os
import shutil

# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции. 


def fill_random_number(filename, count_number):
    with open(filename, 'a') as file:
        for _ in range(count_number):
            int_num = random.randint(-1000, 1000)
            float_num = random.uniform(-1000, 1000)
            file.write(f"{int_num} | {float_num}\n")


# fill_random_number('test.txt', 5)

# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

def generaid_pseudonyms():
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    lenght_name = random.randint(4, 7)
    name = [random.choice(vowels)]
    for _ in range(lenght_name - 1):
        name.append(random.choice(vowels + consonants))
    random.shuffle(name)
    
    return ''.join(name).capitalize()

def save_pseudonyms_to_file(filename, num_names):
    with open(filename, 'w') as file:
        for _ in range(num_names):
            file.write(generaid_pseudonyms() + '\n')

# save_pseudonyms_to_file("name.txt", 5)


# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.


def processe_file(numbers_file, names_file, shared_file):
    with open(numbers_file, 'r') as num_file, open(names_file, 'r') as nam_file, open(shared_file, 'w') as shared_file:

        numbers = num_file.readlines()
        names = nam_file.readlines()

        max_len = max(len(names), len(numbers))

        for i in range(max_len):
            int_num, float_num = map(float, numbers[i % len(numbers)].strip().split("|"))
            product = int_num * float_num

            if product < 0:
                output_name = names[i % len(names)].strip().lower()
                shared_file.write(f"{output_name} {abs(product)}\n")
            else:
                output_name = names[i % len(names)].strip().upper()
                shared_file.write(f"{output_name} {round(product)}\n")


# processe_file("test.txt", "name.txt", "shared_file.txt")

# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
     

def create_random_files(extension, min_name_length=6, max_name_length=30,
                        min_file_size=256, max_file_size=4096, num_files=42):
    for _ in range(num_files):
        name_length = random.randint(min_name_length, max_name_length)
        file_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(name_length))
        
        file_name += "." + extension

        file_size = random.randint(min_file_size, max_file_size)
        file_content = bytes(random.getrandbits(8) for _ in range(file_size))

  
        with open(file_name, 'wb') as f:
            f.write(file_content)

    print(f"{num_files} random files with .{extension} extension created!")

# create_random_files('txt')


# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.


def create_files_with_extensions(*extensions, min_name_length=6, max_name_length=30, 
                                min_file_size=256, max_file_size=4096):
    for ext, num in extensions:
        create_random_files(ext, min_name_length, max_name_length, min_file_size, max_file_size, num)
        print(f"{num} random files with .{ext} extension created!")

# create_files_with_extensions(('txt', 10), ('jpg', 5), ('pdf', 7))

# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

def sort_files(directory="."):
  
    categories = {
        "Video": [".mp4", ".mkv", ".flv", ".avi"],
        "Images": [".jpg", ".jpeg", ".png", ".bmp", ".gif"],
        "Text": [".txt", ".pdf", ".doc", ".docx"],
    }

 
    for category in categories:
        if not os.path.exists(os.path.join(directory, category)):
            os.makedirs(os.path.join(directory, category))

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

      
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]

            for category, extensions in categories.items():
                if file_extension in extensions:
                    shutil.move(file_path, os.path.join(directory, category, filename))
                    break


sort_files("/Users/radiant5/Desktop/GBPython2.0")
