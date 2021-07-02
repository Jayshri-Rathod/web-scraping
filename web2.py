from web import movie_scrap
import json
import pprint

data=movie_scrap()
def group_by_year(movies):
    i=0
    while i<len(movies):
        j=i+1
        while j<len(movies):
            if movies[i]["year"]>movies[j]["year"]:
                c=movies[i]["year"]
                movies[i]["year"]=movies[j]["year"]
                movies[j]["year"]=c
            j+=1
        i+=1  
    list1=[]
    for i in movies:
        if i["year"] not in list1:
            list1.append(i["year"])
    dict1={i:[]for i in list1}
    for i in movies:
        for j in dict1:
            if j==i["year"]:
                dict1[j].append(i)
    with open("my_file_2.json","w")as file:
        json.dump(dict1,file,indent=4)
    return dict1
group_by_year(data)
