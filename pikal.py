from bs4 import BeautifulSoup
import requests
import json
import os
from os import path
import pprint


def pikal_name_scraped():
    if os.path.isfile("pickal1.json"):
        with open("pickal1.json","r")as read_file:
            data = json.load(read_file)
            return data
    else:
        url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
        api1=requests.get(url)
        soup=BeautifulSoup(api1.text,"html.parser")
        product=soup.find("div",class_="_1gX7")
        pro_duct=product.span.get_text()
        split1=pro_duct.split(" ")
        split2=int(split1[1])
        new_split=split2//32+1
        list1=[]
        pickal_i=1
        position=0
        while pickal_i<=new_split:
            url2="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(pickal_i)
            api=requests.get(url2)
            soup=BeautifulSoup(api.text,"html.parser")
            pickal=soup.find("div",class_="_3RA-")
            pickal_name=pickal.find_all("div",class_="UGUy")
            pickal_price=pickal.find_all("div",class_="_1kMS")
            pickal_url=pickal.find_all("div",class_="_3WhJ")
            i=0
            while i<len(pickal_name):
                position+=1
                name=(pickal_name[i].get_text())
                price=(pickal_price[i].get_text())
                url1=(pickal_url[i].a["href"])
                url_1="https://paytmmall.com"+(url1)
                my_dict={"position":position,"name":name,"price":price,"url1":url_1}
                list1.append(my_dict)
                i+=1 
            pickal_i+=1             
        with open("pickal1.json","w")as f:
            json.dump(list1,f,indent=4)
        return list1
pikal_name_scraped()



