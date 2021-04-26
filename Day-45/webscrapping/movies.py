
from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
URL = "https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512"

response = requests.get(URL)
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")
#print(soup.prettify())

all_movies = soup.find_all(name="h1", class_="list-item__title")
#movies = soup.find_all(name="h3")
list_movies = [movie.getText() for movie in all_movies]


movies = list_movies[::-1]

with open('movies.txt', mode='w') as file:
    for movie in movies:
        file.write(f"{movie}\n")
