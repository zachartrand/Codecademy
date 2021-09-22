import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("survey.csv")
"""
# Plots Response vs Age Range with a bar for each Gender.
sns.barplot(
    data = df,
    x = 'Age Range',
    y = 'Response',
    hue = 'Gender',
)
"""
# Plots Response vs Gender with a bar for each Age Range.
sns.barplot(
    data = df,
    x = 'Gender',
    y = 'Response',
    hue = 'Age Range',
)

plt.show()
