from OmaMoodul import *
laused=[]
while True:
    menu=input('1-loeme failist \n2-Salvestame failisse \n3-Sõnade tõlkimine \n4-Vaata sõnastikku5-Parandage viga sõnastikus\n6-Harjutus\n')

    while menu.isdigit()==False:
        menu=input("Kirjuta ainult need numbrid, mis on ")
    print()
    if menu=="1":
        laused=Loe_failist("Laused.txt")
        for line in laused:
            print(line)
    elif menu=="2":
        line=input("Lisa lause: ")
        laused.append(line)
        Kirjuta_failisse("Laused.txt",laused)
    elif menu=="3":
        tolk("rus.txt","est.txt")
    elif menu=="4":
        laused=Loe_failist("rus.txt")
        for line in laused:
            print(line)
        print()
        laused=Loe_failist("est.txt")
        for line in laused:
            print(line)
    elif menu=="5":
        parandama("rus.txt","est.txt")
    elif menu=="6":
        harjutus("rus.txt","est.txt")
