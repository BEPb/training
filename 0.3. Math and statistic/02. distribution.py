# Pyton 3.9

# Пример биномиального распределения

# В эксперименте подбрасываем монетку определенное количество раз. Хотим построить распределение вероятности выпадения
# орла

import numpy as np
import matplotlib.pyplot as plt

# сколько раз бросаем монетку
attemptsNumber = 20

# вероятность "успеха" - выпадения орла
p = 0.5

probabilityValues = []

for k in range(0, attemptsNumber):
    probabilityValue = np.math.factorial(attemptsNumber) * p ** k * (1 - p) ** (attemptsNumber - k) / np.math.factorial(
        attemptsNumber - k) / np.math.factorial(k)

    probabilityValues.append(probabilityValue)
    print('Значение для k = {}: {}'.format(k + 1, probabilityValue))

probabilityValues

plt.plot(probabilityValues)
plt.show()

sum(probabilityValues)

### Примеры распределений по росту
# Данные взяты отсюда https://people.sc.fsu.edu/~jburkardt/data/csv/hw_25000.csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import norm

data = pd.read_csv('hw_25000.csv', names=['index', 'height_inches', 'weight_pounds'], header=0)
data.head()

# переводим высоту в сантиметры

data['height'] = data['height_inches'] * 2.54
data.head()

len(data)

plt.hist(data['height'], bins=50)
plt.show()

# проверим "нормальность" нашего распределения с помощью QQ-plot

stats.probplot(data['height'], dist="norm", plot=plt)
plt.show()

data['height'].plot.density()

### Стандартизация (z-преобразование)

np.mean(data['height']), np.std(data['height'])

zHeight = stats.mstats.zscore(data['height'])

np.mean(zHeight), np.std(zHeight)

customHeight = 185

zScore = (customHeight - np.mean(data['height'])) / np.std(data['height'])
print(zScore)

1 - stats.norm.cdf(zScore)

# доверительный интервал для заданного уровня значимости

stats.norm.interval(0.95)

stats.norm.interval(0.99)

### Доверительный интервал

sample = data.head(100)

se = np.std(sample['height']) / np.sqrt(len(sample['height']))
print(se)

confidenceCoef = stats.norm.interval(0.95)[1]

(np.mean(sample['height']) - confidenceCoef * se, np.mean(sample['height']) + confidenceCoef * se)
