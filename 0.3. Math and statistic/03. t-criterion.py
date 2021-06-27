# Сравнение средних

from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# среднее значение X равно некоторому известному значению m

# t-статистика

### Одновыборочный критерий
# берется выборка из 25000 значений, где указан их рост и вес
data = pd.read_csv('hw_25000.csv', names=['index', 'height_inches', 'weight_pounds'], header=0)
data['height'] = data['height_inches'] * 2.54  # преобразуем дюймы в сантиметры в выборке
print(data.head())

data['sample'] = data['height'] + 3  # создадим еще одну выборку где значения роста больше на 3см
print(data.head())

bins = np.linspace(150, 190, 50)

plt.hist(data['height'], bins, alpha=0.5)
plt.hist(data['sample'], bins, alpha=0.5)
plt.show()

plt.hist(data['sample'].head(20), bins)  # работа только с 20-ю значениями из выборки
plt.show()

sample = data['sample'].head(20).tolist()
sample

np.mean(sample)

data['height'].mean()

stats.ttest_1samp(sample, data['height'].mean())

### Двухвыборочный критерий


plt.hist(data['sample'].head(20), bins, alpha=0.5)
plt.hist(data['height'].tail(20), bins, alpha=0.5)
plt.show()

sampleHead = data['sample'].head(20).tolist()
sampleTail = data['height'].tail(20).tolist()

sampleHead

sampleTail

stats.ttest_ind(sampleHead, sampleTail)
