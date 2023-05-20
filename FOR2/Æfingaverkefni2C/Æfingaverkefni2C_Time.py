sek=1
minuta=0
while minuta<5:
    try:
        #sys.stdout.write(str(sek)+ " ")
        #sys.stdout.flush()
        print(sek)
        time.sleep(0.1)
        sek+=1
        if sek==60:
            minuta+=1
            print("\n",minuta,"mín")
            sek=1
    except KeyboardInterrupt: #control c
        minuta=100
