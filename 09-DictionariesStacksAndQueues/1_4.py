person = {
   "name": "Marcin",
   "surname": "Banach",
   "age": 20,
   "hobby": ["swimming","excursions"],
   "married": False,
   "phone":{"landline":"123444321","mobile":"777888999"}
}
print(person["name"])
print(person["hobby"])
for key,value in person.items():
    print(f"{key} : {value}")
person["surname"] = "nowak"
person["married"] = True
person["gender"] = "male"
person["hobby"].append("bicycle")
person["phone"]["workphone"] = '313131444'
for key,value in person.items():
    print(f"{key} : {value}")