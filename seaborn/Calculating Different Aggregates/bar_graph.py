import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("survey.csv")
# print(df)
sns.barplot(
    data=df,
    x='Gender',
    y='Response',
    estimator=np.median,
    ci='sd',
)

plt.show()
