from bs4 import BeautifulSoup
import requests
import json
import re

def movie_scrap():
    url="https://www.imdb.com/india/top-rated-indian-movies/"
    x=requests.get(url)
    soup=BeautifulSoup(x.text,"html.parser")
    list=[]
    movie_find=soup.find("div",class_="lister")
    movie_find_1=movie_find.find("tbody",class_="lister-list")
    movie_find_2=movie_find_1.find_all("tr")
    position=0
    for i in movie_find_2:
        position=position+1
        movie_name=i.find("td",class_="titleColumn").a.get_text()
        name=movie_name
        movie_year=i.find("td",class_="titleColumn").span.get_text()[1:5]
        # year1=(re.sub('[()]','',movie_year))
        year=int(movie_year)
        movie_rate=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        rate=float(movie_rate)
        movie_link=i.find("td",class_="titleColumn").a['href']
        movie_url="https://www.imdb.com"+str(movie_link)
        url1=movie_url
        my_dict={"position":position,"name":name,"year":year,"rate":rate,"url":url1}
        list.append(my_dict)
        # dict={"movies":list}
        with open("my_file.json","w")as f:
            json.dump(list,f,indent=4)
    return list
movie_scrap()


