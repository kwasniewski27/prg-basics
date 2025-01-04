temp = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
positive = filter(lambda city: temp[city]>0, temp)
positive_cities = " ".join(positive)
print(positive_cities)