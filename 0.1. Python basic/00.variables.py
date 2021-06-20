# python 3.9

## Работа с переменными
# python -m notebook    -  для запуска jupyter notebook

# длинные переменные и названия функций можно записывать разными способами
snake_case_integer = 5  # присваиваем значение переменной
print(snake_case_integer)  # выведем значение переменной
print(type(snake_case_integer))  # выведем тип переменной int - целочисленное
print(" ")  # пустая строка для вывода

camelCaseString = 'строка из слов'  # присваиваем значение переменной
print(camelCaseString)  # выведем значение переменной
print(type(camelCaseString))  # выведем тип переменной str - строчная
print(" ")  # пустая строка для вывода

# первый элемент всегда имеет номер 0
# например, первая буква слова

print(camelCaseString[0])  # выведм первый элемент строки
# разделитель - точка

floatNumber = 3.14
print(floatNumber)
print(type(floatNumber))  # выведем тип переменной float - дробь