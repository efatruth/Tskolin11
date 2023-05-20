#livinus felix bassey
#Skilaverkefni4
#24.10.2018


class Nemi():
    def __init__(self, kenni,naf,ky,heimilis,sima,email):
        self.kennitala = kenni
        self.nafn = naf
        self.kyn = ky
        self.heimilisfang = heimilis
        self.simanumer = sima
        self.netfang = email

    def get_kennitala(self):
        return self.kennitala
    def get_nafn(self):
        return self.nafn
    def get_kyn(self):
        return self.kyn
    def get_heimilisfang(self):
        return self.heimilisfang
    def get_simanumer(self):
        return self.simanumer
    def get_netfang(self):
        return self.netfang

    def set_kennitala(self,nyttKennitala):
        self.kennitala = nyttKennitala
    def set_nafn(self,nyttNafn):
        self.nafn = nyttNafn
    def set_kyn(self,nyttKyn):
        self.kyn = nyttKyn
    def set_heimilisfang(self,nyttHeimilisfang):
        self.heimilisfang = nyttHeimilisfang
    def set_simanumer(self,nyttSimanumer):
        self.simanumer = nyttSimanumer
    def set_netfang(self,nyttNetfang):
        self.netfang = nyttNetfang

    def __str__(self):
        return "NEMI:" "Kennitolu:" + str(self.kennitala) +" Nemandi "+ self.nafn +" kynlif: " + self.kyn +" heima á: " +self.heimilisfang +" simatala:" + str(self.simanumer) +" simatala:" +(self.netfang)


class Grunnskolanemi(Nemi):
    def __init__(self,kenni,naf,ky, heimilis,sima,email,forrada,nafnSkola):
        Nemi.__init__(self, kenni,naf,ky,heimilis,sima,email)
        self.forradamadur = forrada
        self.nafnSkola = nafnSkola
    def __str__(self):
         return "Grunnskolanemi:" "Kennitolu:" + str(self.kennitala) +" heitir "+ self.nafn +" kynlif er: " + self.kyn +" heima: " +self.heimilisfang +" simatala:" + str(self.simanumer) +" simatala:" +(self.netfang)+" forreldra:" +(self.forradamadur)+" skóla:" +(self.nafnSkola)


class  Framhaldskolanemi(Nemi):
    def __init__(self,kenni,naf,ky, heimili,sima,email,brautar,busetu):
        Nemi.__init__(self, kenni,naf,ky,heimili,sima,email)
        self.brautarheiti  = brautar
        self.busetustyrkur  = busetu
    def __str__(self):
         return "Framhaldskolanem: ""Kennitolu:" + str(self.kennitala) +" Nemandi "+ self.nafn +" kynlif: " + self.kyn +" heima: " +self.heimilisfang +" simatala:" + str(self.simanumer) +" simatala:" +(self.netfang)+" braut:" +(self.brautarheiti)+" busett:" +(self.busetustyrkur)

class   Haskolanemi(Nemi):
    def __init__(self,kenni,naf,ky, heimili,sima,email,stig,buset):
        Nemi.__init__(self, kenni,naf,ky,heimili,sima,email)
        self.stigNams  = stig
        self.busetustyrkur = buset

    def __str__(self):
         return "Haskolanemi: ""Kennitolu:" + str(self.kennitala) +" Nemandi "+ self.nafn +" kynlif: " + self.kyn +" heima: " +self.heimilisfang +" simatala:" + str(self.simanumer) +" simatala:" +(self.netfang)+" stigur:" +(self.stigNams)+" busetti:" +(self.busetustyrkur)

print("-----1---")
nemi1 = Nemi(2102958989, "levinson", "KK", "havallagata 10", 7704848, "levin@yahoo.com")
print(nemi1.nafn)
print(nemi1)

print("-----2------")
#kenni,naf,ky, heimilis,sima,email,forrada,nafnSkola
grunnskolanemi1 = Grunnskolanemi(1102158989, "Palli", "kk","Aðalstræti 16", 5992467,"pall@hotmail.live", "Guðmundison", "Rimaskóli")
print(grunnskolanemi1)


print("-----3--------")
#inheritance from nema er:kenni,naf,ky, heimilis,sima,email, lika með :brautarheiti ,busetustyrkur
framhaldskolanemil = Framhaldskolanemi(1102158129, "jane","kvk","hátevegur 20", 7989467,"jane@yahoo.com", "upplysingtækni", "busetinn")
print(framhaldskolanemil)


print("-----4--------")
#inheritance from nema er:kenni,naf,ky, heimilis,sima,email, lika með :stigNams ,busetustyrkur
haskolanemil = Haskolanemi(1102158467, "luka", "KK","gótunatrin 67", 8924667,"luka@hotmail.live",".þrjú", "busetil")
print(haskolanemil)








