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