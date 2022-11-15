# Line plot med Seaborn

# Imports
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

sns.set(style='darkgrid')

# Data
tips = sns.load_dataset('tips')
print(tips.head())

# Line Plot
sns.lineplot(x='total_bill', y='tip', data=tips)
plt.show()


sns.lmplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")
plt.show()

plt.pie(lang_slices, labels=label_s)

plt.pie(to)