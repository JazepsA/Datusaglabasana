import json

try:
    with open("people_data.json","r",encoding="utf-8") as file:
        people=json.load(file)


except FileExistsError:
    people=[]

while True:
    name=input("Ievadiet vārdu: ")
    age=input("Ievadiet vecumu: ")
    city=input("Ievadiet pilsētu: ")

    people.append({
        "name":name,
        "age":age,
        "city":city
    })

    another=input("Vai v'elaties pievienot v'el vienu cilvēku? (jā/nē)").strip().lower()
    if another !="jā":
        break
with open("people_data.json","w",encoding="utf-8") as file:
    json.dump(people,file,indent=4)


print("Dati ir veiksmīgi saglabāti JSON failā! ")

print("Cilveku jaunaki par 18")
for person in people:
    if int(person["age"]) >=18:
        print(f"Vārds : {person['name']}, Vecums: {person['age']},Pilsēta: {person['city']}")
    

print("Cilveku kas dzivo r")

for person in people:
    if person["city"] [0] == "R":
        print(f"Pilsetas, kuras sakas ar burtu R: {person['city']}")