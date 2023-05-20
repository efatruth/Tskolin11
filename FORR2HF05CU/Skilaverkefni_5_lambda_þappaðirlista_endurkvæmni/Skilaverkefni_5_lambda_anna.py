Dæmi 9(hafið þennan lið í sér skjali)
Til er mörg söfn í python. Eitt af þessum söfnum er tkinter.py. prófið að importa það og gerið eftirfarandi forrit:



Kóðinn lítur svona út:


Hér er annar kóði. Prófið að keyra hann
from tkinter import *
root =Tk()#auður gluggi
topFrame=Frame(root)
one=Label(root,text="einni",bg="red",fg="red")
two=Label(root,text="einni",bg="yellow",fg="blue")
one.pack(fill=X)
two.pack(side=LEFT,fill=Y)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)
button1=Button(topFrame,text="ýttu á mig",fg="red")
button2=Button(topFrame,text="button2",fg="blue")
button3=Button(topFrame,text="button2",fg="yellow")
button4=Button(bottomFrame,text="button2",fg="purple")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
theLabel=Label(root,text="hér er ég")#búa til merkjamiða með ákveðnum texta staðsettan á formin
theLabel.pack()#settu það inn
root.mainloop()#heldur glugganum opnum birtist aftur og aftur

