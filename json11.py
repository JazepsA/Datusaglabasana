import json

data= {
    "name":"Anna",
    "age": 25,
    "city":"Riga"
}

with open("data.json","w",encoding="utf-8") as file:
    json.dump(data,file,indent=4)

print("Pilseta:", data["city"])


people=[
    {"name":"Janis","age": 30,"city": "Riga"},
    {"name":"Anna","age": 25,"city": "Jelgava"},
    {"name":"Peteris","age": 40,"city": "Liepaja"},   
]

with open("people.json","r") as file:
    izvada=json.load(file)

print(izvada)
print("Cilvēki vecāki par 30 gadiem:")

for person in izvada:
    if person["age"] > 30:
        print(person["name"])

new_person={"name":"Laura","age":20,"city":"Sigulda"}
people.append(new_person)

with open("people.json","w") as file:
    json.dump(people,file,indent=4)


kop=0
vid=0
skaits=0
with open("products.json","r") as file:
    data=json.load(file)

    for i in data:
        kop+= i["price"]
        skaits += 1

vid=kop/ skaits

print(f"videjais ir {vid}")



