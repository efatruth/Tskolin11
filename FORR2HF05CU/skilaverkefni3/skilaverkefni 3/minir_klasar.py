#livinus felix bassey
#Skilaverkefni2
#10.09.2018


class Lager_hlutur:

    def __init__(self, num,teg,fjol,ver):
        self.numer = num
        self.tegund = teg
        self.fjoldi = fjol
        self.verd = ver

        alltsedla = Lager_hlutur.alltsedla+1

    def verdReikllut(self):
        result = self.fjoldi * self.verd #her vanta koda
        return result


    def prenta_lager_hlut(self):
        print(self.numer,self.tegund,self.fjoldi,self.verd) #her vanta koda self.tala1 * self.tala2
            
