# python 3.9

# Map и lambda -функции
# map - применяет функцию к каждому элементу листа
print("Map и lambda -функции")

nums = [1, 2, 3, 4, 5]  # создаем лист

def square(x):  # создаем функцию возведения в квадрат
    return x ** 2

list(map(square, nums))  # применяет функцию square к каждому элементу листа nums
print(list(map(square, nums)))
# [1, 4, 9, 16, 25]


# применение лямбда функции
list(map(lambda x: x ** 2, nums))  # то же самое, но через лямбду-функцию
print(list(map(lambda x: x ** 2, nums)))
#[1, 4, 9, 16, 25]


# если одновременно используется несколько функции также
def cube(x):  # функция возведения в куб
    return x ** 3


for i in range(len(nums)):  # цикл пробегающий по номерам всех элементов списка
    print(list(map(lambda x: x(nums[i]), [square, cube])))  # вывод результата двух функци одной возле другой
#[1, 1]
#[4, 8]
#[9, 27]
#[16, 64]
#[25, 125]

#функция - reduce
print("reduce-функция")

from functools import reduce  # импорт несколько элементов в лябмда функцию

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))


# Словари
print("словари")
stats = {  # создаем словарь, напротив даты - данные
    '2017-05-01': 100,
    '2017-05-02': 101,
    '2017-05-03': 102
}

# обращение к элементу словаря
print(stats['2017-05-01'])

# пройтись по элементам словаря
for key, value in stats.items():
    print(key, value)  # выведет все ключи и значения словаря

# количество ключей
print(len(stats))

# проверка на наличие ключа в словаре
newDate = '2017-05-04'
newDateValue = 103

if newDate in stats:
    print('Ok')

else:
    stats[newDate] = newDateValue
    print("добавляем значение")

print(stats)

#Копирование словарей
newStatsDict = stats
newStatsDict['2017-05-05'] = 200
print(stats)


stats = {
    '2017-05-01': 100,
    '2017-05-02': 101,
    '2017-05-03': 102
}
newStatsDict = stats.copy()
newStatsDict['2017-05-05'] = 200
print(stats)

# проходим по ключам
for key in stats.keys():
    print(key)

# проходим по значениям
for value in stats.values():
    print(value)
newData = {
    '2017-05-02': 999
}
stats.update(newData)
print(stats)


# Словари и листы
test = [1, 0, 0, 1]
predictions = [0.89, 0.34, 0.08, 0.67]

for pairs in zip(test, predictions):  # сравниваем значения двух листов попарно
    print(pairs)



categories = ['Еда', 'Авто', 'Политика']
audience = [100, 200, 300]

category_audience = zip(categories, audience)
for element in category_audience:  # сравниваем значения двух листов попарно
    print(element)
categoriesDict = dict(zip(categories, audience))
print(categoriesDict)




#Регулярные выражения
print("Регулярные выражения")
# https://docs.python.org/2/library/re.html#re.compile
import re  # импортируем функцию регулярного выражения

# шаблон страницы новостей (любые символы, потом / и 8 цифр подряд)
# http://www.petefreitag.com/cheatsheets/regex/

pattern = '.*/[0-9]{8}'  # создаем шаблон любая последовательность символов до '/', затем восем цифр от 0 до 9

prog = re.compile(pattern)  # компилируем шаблон регулярного выражения

# если поставить опцию 'w' при обращении к файлу, то он будет очищен
# если 'a' - данные будут добавлены в конец файла

with open('URLs.txt', 'r') as f:
    for line in f:
        # убираем символ переноса строки для каждой читаемой строчки
        line = line.strip()

        # если текст строки удовлетворяем регулярному выражению pattern, то выводим строку
        if prog.match(line):
            print(line)