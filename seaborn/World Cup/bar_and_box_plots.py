from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')
df["Total Goals"] = df["Home Team Goals"] + df["Away Team Goals"]
# print(df.head())

df_goals = pd.read_csv("goals.csv")
# print(df_goals.head())

sns.set_style("whitegrid")
sns.set_context("poster")

fig, ax = plt.subplots(figsize=(12, 7))
sns.barplot(data=df, x="Year", y="Total Goals")
ax.set_title("World Cup Total Goals Per Year")
plt.show()

sns.set_context("notebook", font_scale=1.25)
fig, ax2 = plt.subplots(figsize=(12, 7))
ax2 = sns.boxplot(data=df_goals, palette="Spectral", x="year", y="goals")
ax2.set_title("Goal distribution")
plt.show()
