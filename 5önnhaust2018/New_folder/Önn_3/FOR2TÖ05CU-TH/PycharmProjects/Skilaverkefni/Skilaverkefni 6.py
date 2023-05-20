#Along A. Loftsson

print("1.")
print()

class Rummal:
    def __init__(self):
        pass

class Kúla(Rummal):
    pass


print()
print("2.")
print()

class Nemi(object):
    def __init__(self, kt, nafn, kyn, heimilisfang, numer, netfang):
        self.kt = kt
        self.nafn = nafn
        self.kyn = kyn
        self.heimilisfang = heimilisfang
        self.numer = numer
        self.netfang = netfang

    def get_value(self):
        return self.kt + " " + self.nafn + " " + self.kyn + " " + self.heimilisfang + " " + self.numer + " " +\
               self.netfang

class Grunnskolanemi(Nemi):
    def __init__(self, kt, nafn, kyn, heimilisfang, numer, netfang, forradamadur, nafnSkola):
        Nemi.__init__(self, kt, nafn, kyn, heimilisfang, numer, netfang)
        self.forradamadur = forradamadur
        self.nafnSkola = nafnSkola

    def upplysingar(self):
        upplysingar = self.get_value()
        upplysingar =  upplysingar + " " + self.forradamadur, self.nafnSkola
        upplysingar = " ".join(upplysingar)
        return upplysingar

class Framhaldskolanemi(Nemi):
    def __init__(self, kt, nafn, kyn, heimilisfang, numer, netfang, brautarheiti, busetustyrkur):
        Nemi.__init__(self, kt, nafn, kyn, heimilisfang, numer, netfang)
        self.brautarheiti = brautarheiti
        self.busetustyrkur = busetustyrkur

    def upplysingar(self):
        upplysingar = self.get_value()
        upplysingar =  upplysingar + " " + self.brautarheiti, self.busetustyrkur
        upplysingar = " ".join(upplysingar)
        return upplysingar



class Haskolanemi(Nemi):
    def __init__(self, kt, nafn, kyn, heimilisfang, numer, netfang, degree, namslan):
        Nemi.__init__(self, kt, nafn, kyn, heimilisfang, numer, netfang)
        self.degree = degree
        self.namslan = namslan

    def upplysingar(self):
        upplysingar = self.get_value()
        upplysingar =  upplysingar + " " + self.degree, self.namslan
        upplysingar = " ".join(upplysingar)
        return upplysingar



kt = "1101003610"
nafn = "Jón"
kyn = "KK"
heima = "Austurstræti 1"
numer = "58-12345"
netfang = "name@example.com"
forradamadur = "Jón Arelius"
nafnSkola = "Tækniskólinn"
student1 = Nemi(kt,nafn,kyn,heima,numer,netfang)
print("Mjög gróf sýning, en það birtir í röð:")
print("Kennitala, Nafn, Kyn, Heimilisfang, Símanúmer, Tölvupóstur, Auka-upplýsingar 1, Auka-upplýsingar 2.")
print()
print(student1.get_value())
student2 = Grunnskolanemi(kt, nafn, kyn, heima, numer, netfang, forradamadur, nafnSkola)
print(student2.upplysingar())
student3 = Framhaldskolanemi("3009002830", "Ari Smásson", "KK", "Faxabraut 20", "421-5050", "ekkigaman@tskoli.is",
                             "Málabraut", "Já")
print(student3.upplysingar())

student4 = Haskolanemi("2112993641", "Jakob Jásson", "KVK", "Dýraleit 35", "339-2125", "alltafcool@hotmail.com", "BSc",
                       "Já")
print(student4.upplysingar())

