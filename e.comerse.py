from bs4 import BeautifulSoup
import requests
import json

def E_commerce():
    url="https://webscraper.io/test-sites"
    res=requests.get(url)
    soup=BeautifulSoup(res.text,"html.parser")
    enter1=soup.find("div",class_="container test-sites")
    computer_name=enter1.find_all("div",class_="col-md-7 pull-right")
    list1=[]
    position=0
    for i in computer_name:
        position+=1
        site_name=i.find("h2",class_="site-heading").a.get_text().strip()
        name=site_name
        url1=i.find("h2",class_="site-heading").a["href"]
        url2="https://webscraper.io"+str(url1)
        url3=url2
        my_dict={"position":position,"name":name,"url":url3}
        list1.append(my_dict)
        with open("my_commerse.json","w")as file:
            json.dump(list1,file,indent=4)
    return list1
E_commerce()

        