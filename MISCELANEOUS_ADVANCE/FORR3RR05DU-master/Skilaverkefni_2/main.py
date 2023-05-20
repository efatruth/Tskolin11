"""
def samnefnari(n, m):
    if n%m == 0:
        return m
    elif n%m == 1:
        return 1
    return samnefnari(m, n%m)

print(samnefnari(25,85))

def thversumma(n):
    if not n:
        return 0
    else:
        return int(str(n)[0]) + thversumma(str(n)[1:])

print(thversumma(10))

def runa(m):
    if m == 1:
        print(1, end=" ")
    else:
        runa(m-1)
        print(str((m**2 + m)//2), end=" ")

"""
def summa(m):
    if m == 0:
        return 0
    return m**2 + summa(m-1)
print(summa(5))
"""
def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')


number = int(input("Enter any decimal number: "))

decimalToBinary(number)
"""
