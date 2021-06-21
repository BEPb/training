# python 3.9
# Практикум по Pandas

import pandas as pd
import numpy as np

# Поэлементные действия с DataFrame
print('')
print("Поэлементные действия с DataFrame")

# зададим два DataFrame
df1 = pd.DataFrame([(0, 1), (2, 3), (4, 5)], columns=['value1', 'value2'])
print(df1)

df2 = pd.DataFrame([(10, 11), (12, 13), (14, 15), (17, 18)], columns=['value1', 'value3'])
print(df2)

# функция сложения
print(df1.add(df2))

# для несовпадающих строк используем значение из fill_value
print(df1.add(df2, fill_value=100))

# combine - выполнение функции
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.combine.html
# выполнение функции func с DataFrame
print(df1.combine(df2, func=lambda x, y: x + y, fill_value=0))

# mul - перемножение
print(df1.mul(df2, fill_value=0))

# div - поэлементное деление DataFrame
print(df1.div(df2, fill_value=17))
# Разность DataFrame
print(df1.sub(df2))

# Корректное копирование DataFrame
print('')
print("Пример не правильного коприрования")
# зададим DataFrame
df1 = pd.DataFrame([(0, 1)], columns=['value1', 'value2'])
print(df1)
# делаем его "копию"
df2 = df1
# Изменяем значение ячейки в "копии"
df2['value1'][0] = 555
print(df2)
# Смотрим что произошло с исходным
print(df1)

# Сделаем "настоящую" копию
print('')
print("Пример правильного коприрования")
df1 = pd.DataFrame([(0, 1)], columns=['value1', 'value2'])
print(df1)
df2 = df1.copy()
# Изменяем значение ячейки в "копии"
df2['value1'][0] = 555
print(df2)
# Смотрим что произошло с исходным
print(df1)

# Сводные таблицы
data = pd.read_csv('train.csv', delimiter=',')
print(data.head())

# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.pivot.html
# index - значения столбца, которые будут в строках
# columns - значения столбца, которые образуют столбцы
# values - значения в ячейках таблицы
# aggfunc - функция, которая будет применена к значениям

# среднее значение столбца 'Age' в разбивке по Sex и Embarked
pd.pivot_table(data, index='Sex', columns='Embarked', values='Age', aggfunc=np.mean)

# если нужно указать несколько столбцов
pd.pivot_table(data, index=['Sex', 'Embarked'], values='Age', aggfunc=np.mean)

# Apply - применить функцию в столбцу или строке
data = pd.read_csv('train.csv', delimiter=',')
data.head(20)


def ageGroup(row):
    """
    Простая функция отнесения возраста к группе
    """

    # проверяем, что значение возраста не равно NaN
    if not pd.isnull(row['Age']):
        if row['Age'] <= 18:
            return 'Child'

        if row['Age'] >= 65:
            return 'Retiree'

        return 'Young'

    # если значение возраста NaN, то возвращаем Undef
    return 'Undef'


# применим функцию ageGroup к DataFrame и выведем результат в отдельный столбец ageGroup

data['ageGroup'] = data.apply(ageGroup, axis=1)
data.head(10)

# Applymap - применяем функцию к каждой ячейке отдельно
# например, устанавливаем формат отображения

df = pd.DataFrame(np.random.randn(10, 3), columns=['first', 'second', 'third'])
print(df)
print(df.apply(lambda x: x ** 2))

# Сохранение DataFrame
data.head()
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html
# разделитель sep по умолчанию запятая
# na_rep - что ставим на место пустых ячеек
# columns - какие столбцы хотим записать
# index - включать ли номер строки

data.to_csv('train_modified.csv', sep=';', na_rep='0', columns=['Survived', 'ageGroup'], index=False)
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_json.html
# при сохранении в JSON может быть несколько вариантов группировки данных

# orient = index - строки имеют вид
# {"0":{"PassengerId":1,"Survived":0,"Pclass":3,"Name":"Braund, Mr. Owen Harris","Sex":"male",
# "Age":22.0,"SibSp":1,"Parch":0,"Ticket":"A\/5 21171","Fare":7.25,"Cabin":null,"Embarked":"S","ageGroup":"Young"}
data.to_json('train_json_index.json', orient='index')

# другие варианты
data.to_json('train_json_columns.json', orient='columns')
data.to_json('train_json_records.json', orient='records')

# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_excel.html
# сохранение в Excel
data.to_excel('train_modified.xlsx', sheet_name='data')

