# Напишите код, который запускается из командной 
# строки и получает на вход путь до директории на ПК.
# 📌Соберите информацию о содержимом в виде объектов namedtuple.
# 📌Каждый объект хранит: ○ имя файла без расширения или название каталога, 
# ○ расширение, если это файл, ○ флаг каталога, ○ название родительского каталога.
# 📌В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
import sys
import logging
from collections import namedtuple


logging.basicConfig(filename='directory_info.txt', level=logging.INFO, format='%(message)s')


ItemInfo = namedtuple('ItemInfo', ['name', 'extension', 'is_dir', 'parent'])


def get_item_info(item_path, parent_dir):
    base_name = os.path.basename(item_path)
    name, extension = os.path.splitext(base_name)

    if os.path.isdir(item_path):
        return ItemInfo(name=base_name, extension=None, is_dir=True, parent=parent_dir)
    else:
        return ItemInfo(name=name, extension=extension.lstrip('.'), is_dir=False, parent=parent_dir)
    


def gather_dirictory_info(directory_path):
    parent_dir = os.path.basename(directory_path)

    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path,item)
        item_info = get_item_info(item_path, parent_dir)
        logging.info(item_info)

        if item_info.is_dir:
            gather_dirictory_info(item_path)


def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    directory_path = sys.argv[1]


    try:
        gather_dirictory_info(directory_path)

    except Exception as e:
        print(f'Ошибка запуска {e}')


if __name__ == '__main__':
    main()
