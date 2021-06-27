# Сравнение средних

from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# среднее значение X равно некоторому известному значению m

# t-статистика

### Одновыборочный критерий

data = pd.read_csv('hw_25000.csv', names=['index', 'height_inches', 'weight_pounds'], header=0)
data['height'] = data['height_inches'] * 2.54
data.head()

data['sample'] = data['height'] + 3
data.head()

bins = np.linspace(150, 190, 50)

plt.hist(data['height'], bins, alpha=0.5)
plt.hist(data['sample'], bins, alpha=0.5)
plt.show()

plt.hist(data['sample'].head(20), bins)
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
