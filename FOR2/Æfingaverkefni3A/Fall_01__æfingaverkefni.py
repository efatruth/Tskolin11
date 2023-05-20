'''
Copyright 2010 Google Inc.
http://code.google.com/edu/languages/google-python-class/
'''
# Munið eftir að setja nafn ykkar hér og dagsetningu+ smá komment í kóðann
# Æfingar í föllum(functions)
# Eina sem þið þurfið að gera er að klára föllin
# main()fallið keyrir nokkur test til að sjá hvort aðferðin sé rétt
# Ef fallið er rétt skrifast út OK annars X


# A. suma_tveir
# Þeta fall á að skila summu tveggja talna
# suma_tveir(1,1) skilar 2
#  og suma_tveir(10, 5) skilar 15
def summa_tveir(a, b):
    # +++Þinn kóði+++
    return  a + b

# B. Kleinuhringir
# count er fjöldi kleinuhringja(int)
# ef fjöldi kleinuhringja er undir 10 sendir fallið frá sér strenginn
# "fjöldi kleinuhringja er:<count>(Þar sem <count> er fjöldi kleinuhringja
# ef fjöldi kleinuhringja er yfir 10 þá á að skrifast
# margir kleinuhringir
# kleinuhringir(5) skilar strengnum  'fjöldi kleinuhringja er:5'
# kleinuhringir(23) skilar strengnum 'margir kleinuhringir'
def kleinuhringir(count):
    if count < 10:
        return "fjöldi kleinuhringja er:" + str(count)
    else:
        return "margir kleinuhringir"

# C. Báðir endar
# teknir eru fremstu tveir stafirnir af strengnum s og líka tveir síðustu
# dæmi strengur verður stur
# ef strengurinn er minni en 2 stafir skilar fallið tómum streng

def badir_endar(s):
    if len(s) >= 2:
        a=s[0:2]+s[-2]+s[-1]
        return a
    else:
        return ""


# D. fix_start
# fallið tekur við streng og breytir honum þannig
# að fyrstu stafur strengsins er breytt í * nema upphafstafurinn
# t.d. 'babble' breytist í 'ba**le'
# Gengið er útfrá að strengurinn er allavegana einn stafur

def fix_start(s):
    a=s[0]
    s=s[1:len(s)]
    s=s.replace(a,"*")
    s=a+s
    return s


# E. MixUp
# Fallið tekur tvo strengi a og b og skrifar þá út sem einn streng með bil milli a og b
# auk þess er skipt á tveimur fyrstu stöfunum í streng a og b
# dæmi:'mix', pod' -> 'pox mid'
# dæmi: 'dog', 'dinner' -> 'dig donner' 
# Strengirnir mega ekki vera styttri en 2 stafir hver um sig.  

def mix_up(a, b):
    if len(a) < 2 and len(b) <= 2:
        print("strengur a er of stuttur.")
    elif len(b) < 2 and len(a) <= 2:
        print("strengur b er of stuttur.")
    elif len(a) < 2 and len(b) < 2:
        print("strengir a og b eru of stuttir.")
    else:
        c=b[0:2]+a[2:len(a)] + " " + a[0:2]+b[2:len(b)]
        return c 


# F. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    sNot=s.find('not')
    sBad=s.find('bad')
    if sNot < sBad and sNot != -1 and sBad != -1:
            s=s.replace(s[sNot:len(s)],"good"+s[sBad+3:])
    return s


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix,got,expected))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print('summa_tveir')
    # Hver lína skoðar mismunandi gildi
    test(summa_tveir(0,0), 0)
    test(summa_tveir(1,2), 3)
    test(summa_tveir(27, 83), 110)
    test(summa_tveir(100, 99), 199)


    print()
    print('kleinuhringir')
    test(kleinuhringir(4), 'fjöldi kleinuhringja er:4')
    test(kleinuhringir(9), 'fjöldi kleinuhringja er:9')
    test(kleinuhringir(10), 'margir kleinuhringir')
    test(kleinuhringir(99), 'margir kleinuhringir')

    print()
    print('báðir_endar')
    test(badir_endar
         ('spring'), 'spng')
    test(badir_endar('Hello'), 'Helo')
    test(badir_endar('a'), '')
    test(badir_endar('xyz'), 'xyyz')

    print()
    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print()
    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")


if __name__ == "__main__":
    main()
