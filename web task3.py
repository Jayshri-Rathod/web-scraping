from web import movie_scrap
from web2 import group_by_year
import json

Data=movie_scrap()
def group_by_decade(movies):
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
    new_list=[]
    for i in movies:
        year=i["year"]
        modul=year%10
        substract=year-modul
        if substract not in new_list:
            new_list.append(substract) 
    new_list.sort()
    dict2={a:[]for a in new_list}
    for i in movies:
        for j in new_list:
            if i["year"]>=j and i["year"]<(j+10):
                dict2[j].append(i)           
    with open("my_file_3.json","w")as file:
        json.dump(dict2,file,indent=4)
    return dict2
group_by_decade(Data)










                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       








# data=movie_scrap()
# def group_by_decade(movies):
#     i=0
#     while i<len(movies):
#         j=i+1
#         while j<len(movies):
#             if movies[i]["year"]>movies[j]["year"]:
#                 c=movies[i]["year"]
#                 movies[i]["year"]=movies[j]["year"]
#                 movies[j]["year"]=c
#             j+=1
#         i+=1 
#     key_list=[1950,1960,1970,1980,1990,2010,2020]
#     dict2={a:[]for a in key_list}
#     for l in movies:
#         for i in dict2:
#             if l["year"]==i:
#                 dict2[i].append(l)
#     with open("my_file_3.json","w")as file:
#         json.dump(dict2,file,indent=4)
#     return dict2
# group_by_decade(data)

