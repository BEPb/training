# python 3.9
# Какое количество различных слов русского языка можно составить из букв слова «питон»?
# Примеры: кот, стекло, лето. Используйте любой словарь русского языка.

import collections  # предоставляет специализированные типы данных, на основе словарей, кортежей, множеств, списков

word = 'питон'  # задаем исходное слово
my_world = {i:word.count(i) for i in word}  # используея cont преобразуем слово в словарь с перечнеи колличества букв
print(my_world)  # вывод содержимого словаря

list_worlds = []  # создаем пустой список

with open('word_rus_ansi.txt', 'r') as f:  # читаем файл
    for line in f:  # по строчно обращаемся к файлу

        line = line.strip()  # убираем символ переноса строки для каждой читаемой строчки

        if len(collections.Counter(my_world) & collections.Counter(line)) == len(line):

            list_worlds.append(line)



print(list_worlds)
print(len(list_worlds))

# line = {'р':1,'о':1,'с':1,'b':1}
# print(len(line))
#
#
# print(collections.Counter(my_world) & collections.Counter(line))
# print(len(collections.Counter(my_world) & collections.Counter(line)))