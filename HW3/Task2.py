# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
#  В результирующем списке не должно быть дубликатов.
# my_list = [1, 2, 3, 4, 2, 5, 6, 7, 3, 8, 9, 9, 10]
# my_dict = {}

# for i in my_list:
#     if i not in my_dict:
#         my_dict[i] = 1
#     else:
#         my_dict[i] += 1

# duble_list = list({i for i in my_list if my_dict[i] > 1})
# print(duble_list)


# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
#  Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии 
# или из документации к языку.
# import string
# text = """
# Python is an interpreted high-level general-purpose programming language. Python's design philosophy 
# emphasizes code readability with its notable use of significant indentation. Its language constructs as 
# well as its object-oriented approach aim to help programmers write clear, logical code for small and 
# large-scale projects. Python is dynamically-typed and garbage-collected. It supports multiple programming 
# paradigms, including structured (particularly, procedural), object-oriented, and functional programming. 
# Python is often described as a "batteries-included" language due to its comprehensive standard library.
# """

# translator = str.maketrans('', '', string.punctuation)
# text = text.lower().translate(translator)
# words = text.split()


# word_count = {}
# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1
    
 
# sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
# print(sorted_words[:10])


# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

def backpack_combinations(items, max_weight):
    if not items:
        return [[]]

    first_item, first_weight = list(items.items())[0]

    remaining_items = {k: v for k, v in items.items() if k != first_item}

    without_first = backpack_combinations(remaining_items, max_weight)

    with_first = []
    if first_weight <= max_weight:
        for subset in backpack_combinations(remaining_items, max_weight - first_weight):
            with_first.append([first_item] + subset)

    return with_first + without_first

items = {
    "Палатка": 5,
    "Спальник": 2,
    "Фонарик": 1,
    "Котелок": 3,
    "Еда": 4
}
max_weight = 10

combinations = backpack_combinations(items, max_weight)
valid_combinations = [comb for comb in combinations if sum(items[i] for i in comb) <= max_weight]
print(valid_combinations)
