1. (2%) Hvað er sauðakóði (pseuodocode) og til hvers er hann notaður?
Sauða kóði er forrit í orðum. Þú mundir bara skrifa hvað forritið á að gera. Það er gott að byrja á að skrifa sauðakóða á stærri forritum áður en þú forritar, forritarinn veit hvernig kóðin myndi verða smíðaður.



___
2. (3%) Skrifaðu forrit í sauðakóða sem umreytir tugakerfistölu í tvíundarkerfistölu. Hér er ekki
verið að biðja um keyranlegt forrit.

Fær tolu dec tölu sendir hana í function sem tjekkar á hvort talan sé stærri en einn. Ef hún er stærri en einn kallar fallið aftur á sjálfan sig með sömu tölu nem floor deild(//) með 2. þegar Talan er orðin minni en 1 prentar hann töluna í fallinu % 2. sem er binary talan.

___
3. (2%) Skoðaðu rununa 1, 4, 9, 16, 25, 36, .... Eins og þú sérð er þetta í raun n
2 þar sem n er stak
í menginu náttúrulegar tölur N = {1, 2, 3, 4,...}. Skrifaðu endurkvæma fallið summa(m) sem
reiknar ∑ 𝑛
𝑚 2
𝑛=1
og skilar summunni. Dæmi: Ef m er 5 þá ætti fallið summa(5) að reikna og
skila 12 + 22 + 32+ 4
2 +52 = 55.

```Pythone

def summa(m):
    if m == 1:
        return 1
    else:
        return m * summa(m-1)

```
___
4. (4%) Skoðaðu vel rununa 1, 3, 6, 10, 15, 21, .... Finndu út mynstur rununnar og skrifaðu
endurkvæma fallið runa(m) sem skrifar m fyrstu stök rununnar á skjáinn. Dæmi: runa(5)
mundi skrifa 1 3 6 10 15 á skjá.

```Pythone

def runa(m):
    if m == 1:
        print(1, end=" ")
    else:
        runa(m-1)
        print(str((m**2 + m)//2), end=" ")
___
5. (2%) Skrifaðu endurkvæma fallið þversumma(n) sem tekur færibreytuna n. Fallið skilar til
baka þversummu n. Dæmi: þversumma tölunnar 12 er 3 eða 1+2=3. Þversumma tölunnar
1206 er 9 eða 1+2+0+6=9. Fallið skilar aðeins einni tölu.

```Pythone

def thversumma(n):
    if not n:
        return 0
    else:
        return int(str(n)[0]) + thversumma(str(n)[1:])
        
```
___
6. (2% ) Skrifaðu endurkvæma fallið samnefnari(n,m) sem tekur tvær heiltölufæribreytur n og
m. Fallið á siðan að finna hæstu tölu sem gengur bæði upp í n og m. Dæmi,
samnefnari(8,12) mundi skila 4 þar sem það er hæsta tala sem gengur bæði upp í 8 og
12. samnefnari(3,13) mundi skila 1 þar sem 1 er hæsta tala sem gengur bæði upp í 3 og
13. samnefnari(12,60) mundi skila 12 þar sem 12 er hæsta tala sem gengur bæði upp í 12
og 60. Fallið skal vera endurkvæmt.
```Pythone

def samnefnari(n, m):
    if n%m == 0:
        return m
    elif n%m == 1:
        return 1
    return samnefnari(m, n%m)

```