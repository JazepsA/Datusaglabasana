dati = ["Pirmais","Otrais","Tresais"]
vards=[]
with open("datip.txt","w",encoding="utf-8") as fail:

    for ieraksts in dati:
        fail.write(ieraksts+ "\n")
    
    #fail.write(input("Ievadiet savu vardu: "+ "\n"))


edieni=["Kartoska","Pelmenjeban","Silka"]

with open("edieni.txt","w",encoding="utf-8") as fail:
    for ediens in edieni:
        fail.write(ediens+ "\n")

'''
skaits=int(input("Ievadiet gramatu skaitu: "))

for i in range(skaits):
    gramata=input("Ievadi GRAMATU: ") 
    autors=input("Īevadiet AUTORU: ")
    gads_izdosanas=input("Ievadiet IZDOSANAS GADU: ")

kopa=[gramata,autors,str(gads_izdosanas)]

with open("gramatas.txt","a",encoding="utf-8") as fail:
    for i in kopa:
        kopa.append(fail.write(i))
'''

with open("gramatas.txt","a",encoding="utf-8") as fail:
    while True:
        jautajums=input('Vai vēlāties ierakstīt vēl vienu grāmatu? (jā / nē) ')
        if jautajums=="jā":
            gramata=input("Ievadi GRAMATU: ") 
            autors=input("Īevadiet AUTORU: ")
            gads_izdosanas=input("Ievadiet IZDOSANAS GADU: ")
            fail.write(f"Grāmatas nosaukums: {gramata} Autors: {autors} Izdošanas gads {gads_izdosanas} \n ")
        else:
            print('Paldies!')
            break 


with open("gramatas.txt","r",encoding="utf-8") as fail:
    for rinda in fail:
        print(rinda.strip())


