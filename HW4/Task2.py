# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.
def split_path_using_iter(path):
    """Разбивает путь на директорию, имя файла и расширение используя iter и next."""
    
    itr = iter(path[::-1])  # Разворачиваем строку, так как будем идти с конца

    extension = []
    for char in itr:
        if char == '.':
            break
        extension.append(char)

    file_name = []
    for char in itr:
        if char == '/':
            break
        file_name.append(char)

    directory = list(itr)

    return ''.join(directory[::-1]), ''.join(file_name[::-1]), ''.join(extension[::-1])


path = "/home/user/documents/file.txt"
print(split_path_using_iter(path))

