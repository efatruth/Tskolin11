# Livinus Felix Bassey
# 03.2.2017
# Skilaverkefni 2


loop = "j" #loopan fyrir while loop
listi = []


val=""

while loop == "j": #Valmynd kemur upp í loopu meðan loop er "j"
    print("[1] Bæta við nýjum í símaskránna.")
    print("[2] Breyta upplýsingum í símaskránni.")
    print("[3] Eyða upplýsingum / eyða línu úr símaskránni.")
    print("[4] Prenta út alla símaskránna ein lína per notanda")
    print("[5] Leita að ákveðnu nafni og prenta upplýsingar um það nafn, sima og kennitölu")
    print("[6] CSV já byrja")
    print("[7] Hætta.")
    val = input("sláður inn númerið sem þér langar að velja: ")#spyr um að velja val


    if val == "6":
        import csv
        '''f = open('postnumer.csv')
        csv_f = csv.reader(f)
        for row in csv_f:
          print(row[0])
          '''
        with open('postnumer.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=';')
            for row in readCSV:
                '''print(row)'''
                '''print(row[0])'''
                print(row[0]+"\t",row[1]+"\t",row[2],)
