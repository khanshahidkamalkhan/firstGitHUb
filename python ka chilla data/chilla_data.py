#import library
import pandas as pd
#import data from file
df = pd.read_csv("data_viz.csv")
print(df)

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
p1=sns.countplot(x="Gender", data=df, hue="Age")
p1.set_title("Plot for Counting")
plt.show()
