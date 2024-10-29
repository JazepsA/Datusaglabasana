with open("vardi.txt","w", encoding="utf-8") as fail:

    while True:
        vards=input("Ievadiet vārdu (ievadiet 'beigt', lai pageigtu): ")

        if vards.lower() == 'beigt':
            break
        fail.write(vards + "\n")


#Lasisana

print("\nievadītie vārdi:")
with open("vardi.txt","r",encoding="utf-8") as fail:
    for rinda in fail:
        print(rinda.strip())