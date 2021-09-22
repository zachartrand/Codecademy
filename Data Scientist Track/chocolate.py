import requests

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup

website_response = requests.get(
    "https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")
website = website_response.content

soup = BeautifulSoup(website, "html.parser")
# print(soup)
ratings = []
for tag in soup.find_all("td", "Rating")[1:]:
    rating = float(tag.get_text())
    ratings.append(rating)

plt.hist(ratings)
plt.show()

companies = []
for tag in soup.select(".Company")[1:]:
    companies.append(tag.get_text())
# print(companies)

chocolate_df = pd.DataFrame.from_dict({"Company": companies, "Rating": ratings})

mean_ratings = chocolate_df.groupby(["Company"]).Rating.mean()
ten_best = mean_ratings.nlargest(10)

percents = []
for tag in soup.select(".CocoaPercent")[1:]:
    percent = int(float(tag.get_text().strip("%")))
    percents.append(percent)

chocolate_df["CocoaPercentage"] = percents

plt.clf()
plt.scatter(
    chocolate_df.CocoaPercentage,
    chocolate_df.Rating,
)
z = np.polyfit(chocolate_df.CocoaPercentage, chocolate_df.Rating, 1)
line_function = np.poly1d(z)

plt.plot(
    chocolate_df.CocoaPercentage,
    line_function(chocolate_df.CocoaPercentage),
    "r--",
)

plt.show()
