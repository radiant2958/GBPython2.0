# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение. 
# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

import os

def rename_files(target_name, digit_count, src_extension, dest_extension, name_range, directory='.'):
    """
    Групповое переименование файлов.
    
    :param target_name: Желаемое конечное имя файлов.
    :param digit_count: Количество цифр в порядковом номере.
    :param src_extension: Расширение исходного файла.
    :param dest_extension: Расширение конечного файла.
    :param name_range: Диапазон сохраняемого оригинального имени.
    :param directory: Директория, в которой нужно переименовать файлы (по умолчанию текущая).
    """

    # Получаем список всех файлов в каталоге с нужным расширением
    all_files = [f for f in os.listdir(directory) if f.endswith(src_extension)]
    
    counter = 0
    
    for file_name in all_files:
        counter += 1
        
        # Возьмите часть оригинального имени
        original_part = file_name[name_range[0]:name_range[1]]
        
        # Создаем новое имя файла
        new_name = f"{original_part}{target_name}{str(counter).zfill(digit_count)}.{dest_extension}"
        
        # Переименовываем файл
        os.rename(os.path.join(directory, file_name), os.path.join(directory, new_name))

# Пример использования:
rename_files("newname", 3, "txt", "log", [3, 6])
