import requests
from bs4 import BeautifulSoup
import time
import csv

page = 1
f = open("anime_list.csv", "a", newline='\n')
write_obj = csv.writer(f)
# write_obj.writerow(["Anime Title"])

while page <= 5:
    res = requests.get(
        f"https://zoro.to/most-popular?page={page}")

    soup = BeautifulSoup(res.text, 'html.parser')

    all_animes = soup.find("div", class_="film_list-wrap")

    anime_list = all_animes.find_all("div", class_="flw-item")

    for anime in anime_list:
        anime_title = anime.find("div", class_="film-detail").h3.a.text
        write_obj.writerow([anime_title])
        print(anime_title)

    page += 1
    time.sleep(12.5)

f.close()
