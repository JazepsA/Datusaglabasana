with open("dati.txt","r",encoding="utf-8") as file: 
    saturs=file.read()#vesela virkne

print(saturs)

with open("dati.txt","r",encoding="utf-8") as file: 
    rindas=file.readlines()
    print(rindas)#uztaisa sarakstu,parveido virkni uz sarakstu
for rinda in rindas:
    print(rinda.strip())

#split 
with open("dati.txt","r",encoding="utf-8") as file: 
    saturs=file.read()
    vardi=saturs.split()#sadala pēc atstarpem
    
print(vardi)
print(len(vardi))#kopejais vardu sk
print(len(set(vardi)))#unikalo vardu sk 

#enumerate

for index,rinda in enumerate(rindas,start=1):
    print(f"{index}:{rinda}")

#noraditais burts

noraditais_burts="k"

with open("dati.txt","r",encoding="utf-8") as file: 
    saturs=file.read()

saturs=saturs.lower()

vardi = saturs.split()

sar=[]

for i in vardi:
    if i [0] == "k":
        sar.append(i)

    else:
        pass

print(sar)
print(len(sar))