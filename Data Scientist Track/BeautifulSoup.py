import requests
from bs4 import BeautifulSoup

webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')
webpage = webpage_response.content

soup = BeautifulSoup(webpage, "html.parser")

print(soup)  # Prints the webpage as a string.
print(soup.p)  # Prints the first <p> tag of the website.
print(soup.p.string)  # Prints the string of the first <p> tag.

for child in soup.div.children:  # Loops through all of the children tags within
    print(child)                 # the first div tag and prints them.

turtle_links = soup.find_all("a")  # Finds all of the <a> tags and saves them as
                                   # a list to the var turtle_links.
links = []

# Go through all of the a tags and get the links associated with them:
for a in turtle_links:
    links.append(prefix+a["href"])

# Define turtle_data:
turtle_data = {}

# Follow each link:
for link in links:
    webpage = requests.get(link)
    turtle = BeautifulSoup(webpage.content, "html.parser")
    turtle_name = turtle.select(".name")[0].get_text()

    stats = turtle.find("ul")
    stats_text = stats.get_text("|")
    turtle_data[turtle_name] = stats_text.split("|")

# Remove all of the newlines from turtle_data:
for _, v in turtle_data.items():
    while '\n' in v:
        v.remove('\n')

# Create the DataFrame:
indices = ["Age (years)", "Weight (lbs)", "Sex", "Breed", "Source"]
turtle_df = pd.DataFrame(turtle_data, index=indices)

# Format the DataFrame so age and weight are numbers, and the other categories
# are only labeled on the rows and columns:
for c in turtle_df:
    age = turtle_df[c]["Age (years)"].split(" ")
    turtle_df[c]["Age (years)"] = float(age[1])

    weight = turtle_df[c]["Weight (lbs)"].split(" ")
    turtle_df[c]["Weight (lbs)"] = float(weight[1])

    sex = turtle_df[c]["Sex"].split(" ")
    turtle_df[c]["Sex"] = sex[1]

    breed = turtle_df[c]["Breed"].split(" ")
    turtle_df[c]["Breed"] = " ".join(breed[1:])

    source = turtle_df[c]["Source"].split(" ")
    turtle_df[c]["Source"] = " ".join(source[1:])

print(turtle_df)
