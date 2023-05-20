def summa(m):
    if m == 0:
        return 0
    return m**2 + summa(m-1)

def runa(n):
    if n == 1:
        print(1, end=" ")
    else:
        runa(n-1)
        print(str((n**2 + n)//2), end=" ")

def thversumma(n):
    if not n:
        return 0
    else:
        return int(str(n)[0]) + thversumma(str(n)[1:])

def samnefnari(n, m):
    if n%m == 0:
        return m
    elif n%m == 1:
        return 1
    return samnefnari(m, n%m)

print()
print("Spurning 3")
print(summa(5)) 

print()
print("Spurning 4")
runa(5) # Fyrstu 5 triangular numbers         

print()
print("\nSpurning 5")
print(thversumma(589)) # 5 + 8 + 9

print()
print("Spurning 6")
print(samnefnari(20, 8)) # Hæsta talan sem gengur upp í tölunum 20 og 8 (4) 
