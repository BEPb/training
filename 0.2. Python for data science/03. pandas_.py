# python 3.9
# Практикум по Pandas

import pandas as pd
import numpy as np


# Типовые действия с DF
data = pd.read_csv('train.csv', delimiter=',')
data.head(3)

# выбрать все строки и подмножество столбцов
dataSelected = data.loc[:3, ['Name', 'Age', 'Cabin']]
print(dataSelected.head())

# добавляем к фильтру строки
# например, с третьей до последней
dataSelected = data.loc[2:15, ['Name', 'Age', 'Cabin']]
dataSelected.head()

# Добавить столбцы
# посчитаем количество символов в столбце Name

data['nameLength'] = data['Age'] ** 0.5
print(data.head())

# удаляем наши вычисления
del data['nameLength']
print(data.head())

# переименование столбца
# параметр inplace указывает, что надо подставить новое значение в самом DataFrame data
data.rename(columns={'Name': 'FIO'}, inplace=True)
data.head()

# можно заменить названия столбцов
# например, иногда русские названия в исходных данных доставляют трудности
data.columns = ['ID', 'Survived', 'Class', 'FIO', 'Gender', 'Age', 'SibSp', 'Parch', 'Ticker number', 'Fare', 'Cabin',
                'Emnarked']
data.head()

pd.DataFrame({}, index=[])

# Действия со строками
data = pd.read_csv('train.csv', delimiter=',')
data.head()

# выбрать нужные строки
# например, со второй по пятую
data.loc[1:4]

# выбор с набором значений
# строки с номерами 1, 2, 3 и 44
dataNew = data.iloc[[1, 2, 3, 44]]

print(dataNew)
dataNew.reset_index(inplace=True)
dataNew.reset_index(inplace=True)
del dataNew['level_0']
pd.DataFrame.reset_index
dataNew

# можно задать маску, по которой будут фильтроваться строки
# например, ID пассажира делится на 2
# mask = (data.PassengerId % 2 == 0 | ~())
# mask[:5]
# data.loc[mask].head()

# Работа с пустыми значениями
data = pd.read_csv('train.csv', delimiter=',')
data.head(10)
# В столбце Age довольно много пустых значений
data.info()
# посмотрим что это за строки
print(data.loc[pd.isnull(data['Age'])].head())

# заменим пустые значения столбца Age на медиану
medianAge = data['Age'].median()
print(medianAge)

# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.fillna.html
data['Age'].fillna(medianAge, inplace=True)

# итак, значение для строки с индексом 5 (было NaN) заменено на среднее
print(data.head(10))

# Сортировка
# сортировка по индексу
data.sort_index(ascending=False).head()

# сортировка по значениям
data.sort_values(by='Age', ascending=False).head()

# сортировка по значениям нескольких столбцов
data.sort_values(by=['Sex', 'Age'], ascending=[True, False]).head()

# Агрегация и группировка
data = pd.read_csv('train.csv', delimiter=',')
data.head()

# число непустых строк в DataFrame
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.count.html
data.count()

# для отдельного столбца
data['Age'].count()

# сумма
data.sum()

# среднее значение
data.mean()

# комбинация функций
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.aggregate.html
data.aggregate(['sum', 'mean'])

# агрегация по столбцам (agg - синоним aggregate)
data.agg({'Age': ['mean'], 'Survived': ['mean', 'sum']})

# группировка по столбцу с вычислением среднего
data.groupby('Sex').mean()

# группировка по нескольким столбцам одновременно
data.groupby(['Sex', 'Age']).mean()

# Объединение DataFrame
# Merge - аналог JOIN в SQL

# заведем два DataFrame

df1 = pd.DataFrame({
    'key1': ['one', 'two', 'three', 'only1'],
    'value': [1, 2, 3, 4]
})
print(df1)

df2 = pd.DataFrame({
    'key2': ['one', 'two', 'three', 'only2'],
    'value': [11, 12, 13, 14]
})

print(df2)

# сохраняем все значения ключей, которые есть в df1
# если нужно несколько столбцов, то пишем left_on = ['key1', ...] и right_on = ['key2', ...]
df1.merge(df2, how='left', left_on='key1', right_on='key2')

# сохраняем все значения ключей, которые есть в df2
df1.merge(df2, how='right', left_on='key1', right_on='key2')

# сохраняем все значения ключей (объединение)
df1.merge(df2, how='outer', left_on='key1', right_on='key2')

# сохраняем только общие значения ключей
df1.merge(df2, how='inner', left_on='key1', right_on='key2')

# Concat - совмещение DataFrame
# объединение DataFrame путем обычного "склеивания"
pd.concat([df1, df2])

# горизонтальное объединение
pd.concat([df1, df2], axis=1)

# Join - объединение по индексу
df1 = pd.DataFrame({
    'key1': ['one', 'two', 'three', 'only1'],
    'value': [1, 2, 3, 4]
},
    index=['0', '1', '2', '3'])
print(df1)

df2 = pd.DataFrame({
    'key2': ['one', 'two', 'three', 'only2'],
    'value': [11, 12, 13, 14]
},
    index=['2', '3', '4', '5'])
print(df2)

# для join надо указать lsuffix и rsuffix

df1.join(df2, how='left', lsuffix='_df1', rsuffix='_df2')
