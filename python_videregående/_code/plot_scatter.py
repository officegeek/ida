# Scatter plot med Seaborn

# Imports
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

sns.set(style='darkgrid')

# Data
tips = sns.load_dataset('tips')
print(tips.head())

# Plot
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.show()

# Hue
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='sex')
plt.show()

# Size
tips['size'].unique()
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='size', size='size', palette='viridis')
plt.show()

# Hue og Size
plt.figure(figsize=(10,7))
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='sex', size='size', sizes=(20,200))
plt.show()

#
sns.relplot(x='total_bill', y='tip', data=tips, hue='day', col='time', row='sex')
plt.show()


