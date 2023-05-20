#Along A. Loftsson 21.09.2017
import time
sekundur = 1 #Byrjar á einni sekúndu.

while sekundur != 0:
        print("Takk") ; time.sleep(sekundur)
        sekundur -= 0.1 #Tek alltaf 0.1 sek af.
        sekundur = round(sekundur,2) #Set round svo að aukastafirnir verða ekki 0.00...776 t.d.

else: #Svo verður það að 0 og hættir á forritinu.
        print("Eigðu góðan dag.")
        print("Í dag er", time.strftime("%d. %B, %A"))
        #Þarf ekki að nota try, því þetta keyrir sjálft og getur ekki farið úrskeiðis.

