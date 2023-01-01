import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
response = requests.get(url)

if response.status_code==200:
    soup = BeautifulSoup(response.text, "lxml")
    print(soup.title.get_text())
    print(soup.a)
    print(soup.a.attrs)

    print(soup.find('li', attrs={"class": "rank01"}))

    rank1 = soup.find('li', attrs={"class": "rank01"})
    print(rank1.a)

    cartoons = soup.find_all('a', attrs={"class": "title"})
    for cartoon in cartoons:
        title=cartoon.get_text()
        link=cartoon["href"]

        print(title,"https://comic.naver.com"+link)
else:
    print(response.status_code)