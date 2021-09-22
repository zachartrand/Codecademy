import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

gradebook = pd.read_csv("gradebook.csv")
# print(gradebook)

sns.barplot(
    data=gradebook,
    x='assignment_name',
    y='grade',
)

plt.show()
