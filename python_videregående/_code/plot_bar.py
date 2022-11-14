# Bar plot med Seaborn

# Imports
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

sns.set(style='darkgrid')

# Data
tips = sns.load_dataset('tips')
print(tips.head())

# Bar Plot
sns.barplot(x='day', y='total_bill', data=tips)
plt.show()
