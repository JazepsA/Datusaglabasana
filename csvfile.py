import csv

#izvadisana
with open("Dati.csv",'r',encoding="utf-8") as file:
    csvFile = csv.reader(file)

    for lines in csvFile:
        print(lines)

#ierakstisana

field = ['Nr','Name','Year']

rows= [['1','Nikita','33'],
['2','Sanita','21'],
['3','Talis','16']]

with open ("student.csv",'w',encoding="utf-8",newline='') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(field)
    csvwriter.writerows(rows)


skaits= 0 
with open("Studenti.csv",'r',encoding="utf-8") as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        if int(lines['Vecums']) > 20:
            skaits += 1
        print(lines)
print(f"Studentu sk. kuriem ir vairak par 20 gadiem: {skaits}")


Nosaukums=[
    ['Produktu nosakukums','Cena','Daudzums']
]

Visi=[
['Ābols','0.5','10'],
['Banāns','0.3','15'],
['Piens','1.2','7']
]

with open ("produkti.csv",'w',encoding="utf-8",newline='') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(Nosaukums)
    csvwriter.writerows(Visi)
print("Darbība notika!")



darbiniekusk=0
kopeja_alga=0
vid_alga=0
with open ("darbinieki.csv",'r',encoding="utf-8",newline='') as file:
    csvFile=csv.DictReader(file)
    csvFile1=csv.reader(file)
    '''
    print(len(csvFile1))
'''
    for i in csvFile:
        kopeja_alga+=int(i['Alga'])
        print(i)
        darbiniekusk += 1
    
vid_alga= kopeja_alga / darbiniekusk

print(kopeja_alga)
print(vid_alga)
        





