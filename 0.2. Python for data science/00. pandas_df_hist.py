# python 3.9
# Практикум по Pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# метод aggregate появился в версии Pandas 0.20.0
# если выдается ошибка AttributeError: 'DataFrame' object has no attribute 'aggregate', то надо обновить Pandas:

# проверяем версию Pandas
print(pd.__version__)

# Создание DataFrame из листов и словарей

dataList = [
    {'date': '2017-07-01', 'value': 100},
    {'date': '2017-07-02', 'value': 200},
    {'date': '2017-07-03', 'value': 300},
    {'date': '2017-07-04', 'value': 400},
    {'date': '2017-07-05', 'value': 500},
]

print(pd.DataFrame(dataList))

# то же самое, но в другом виде
# задаем столбцы

dataDict = {
    'date': ['2017-07-01', '2017-07-02', '2017-07-03', '2017-07-04', '2017-07-05'],
    'value': [100, 200, 300, 400, 500]
}

print(pd.DataFrame.from_dict(dataDict))

# для сохранения порядка следования элементов можем использовать лист вместо словаря

dataDict = [
    ('date', ['2017-07-01', '2017-07-02', '2017-07-03', '2017-07-04', '2017-07-05']),
    ('value', [100, 200, 300, 400, 500])
]

print(pd.DataFrame.from_records(dataDict))

# лист кортежей с указанием заголовков
dataLists = [
    ('2017-07-01', 100),
    ('2017-07-02', 200),
    ('2017-07-03', 300),
    ('2017-07-04', 400),
    ('2017-07-05', 500),
]

headers = ['date', 'value']
pd.DataFrame.from_records(dataLists, columns=headers)
print(pd.DataFrame.from_records(dataLists, columns=headers))

# Создание Series
# можно использовать Numpy для генерации данных
dataNP = np.random.rand(3)  # генерируем 3 дробных числа
print(dataNP)

print(pd.Series(dataNP, index=['first', 'second', 'third']))  # объединение списка и индексами

# Импорт данных для DataFrame из файлов

# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html#pandas.read_csv
# указываем разделитель столбцов в файле
# заголовок у файла есть, но можно задать свои названия (удобно, если изначально они на русском)
# выводим первые 10 строк

data = pd.read_csv('test.csv', delimiter=',')  # считываем данные из формата csv, присваиваем переменной data
print(data.head(10))  # прочитать первые 10 строк
print(data.tail(3))  # прочитать последние 3 строки

# основная информация о нашем DataFrame
# хорошо показывает в каких данных много пропусков
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.info.html

print('')
print("информация о датафремах")
data.info()  # вывод информации о датафрейме

print('')
# статистика DataFrame
# вывод зависит от типа данных
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html

print(data.describe())  # выводит статистические данные

print(pd.Series(['first', 'second']).describe())  # вывод статистики только за первую и вторую запись

# вывод данных по конкретной выборке(столбце дата) и указываем от какого значени до какого
print(pd.Series([np.datetime64('2017-07-01'), np.datetime64('2017-07-02')]).describe(datetime_is_numeric=True))

# Преобразование типов столбцов
print('')
print("Преобразование типов столбцов")
data = pd.read_csv('train.csv', delimiter=',', dtype={'SibSp': str, 'Parch': str})
data.info()

# Распределение значений столбцов
print('')
print("Распределение значений столбцов")
type(data['Pclass'])  # делаем выборку одного столбца, он является типов serios
print(data['Pclass'].head())  # смотрим значения номер класса и номер строки
print(data[
          'Pclass'].value_counts())  # показывает частоту встречаемых значений, т.е. пассажиров 3-го класса 491, а первого 216

# 3    491
# 1    216
# 2    184
# Name: Pclass, dtype: int64


# Форматирование столбцов
# преобразование DataFrame в строку
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_string.html
print('')
print("Форматирование столбцов")

print(data.head().to_string(columns=['Age', 'Fare'], header=False))

# задаем желаемый формат столбцов
formatter = {
    'Age': '{:.0f}'.format,
    'Fare': '{:.5f}'.format,
}

# применяем указанный формат
formattedColumns = data.head().to_string(columns=['Age', 'Fare'], header=False, formatters=formatter)

print(data.head())  # изначально данные в 5 строкази 12 колоннах
print(formattedColumns)  # после преобразования в 5 строках 2 колоннах

print('')
# или форматирование можно провести через цикл

for column in formattedColumns.split('\n'):
    print(column)

# # Гистограмма распределения
h = data['Age'].hist()
plt.show()



