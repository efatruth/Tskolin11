"""
def recur_fibo(n):
    #Recursive function to print
    #fibonacci sequence
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))


nterms = 10 #Þetta sýnir 10 fyrstu raðirnar
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence: ")
    for i in range(nterms):
        print(recur_fibo(i))
"""


#1

def afturkvaem_summa(n):
    print("Nú er n ", n)
    if n ==0:
        return 0
    else:
        return n+afturkvaem_summa(n-1)

num = 16
if num < 0:
    print("Verður að vera plústala")
else:
    print("Summa talnanna er ", afturkvaem_summa(num))


#2

def afturkvaem_summa_oddatala(n):
    print("Nú er n ", n)
    if n == 0 or n == -1:
        return 0
    else:
        if n % 2 == 1: #oddatala
            print("Bingó oddatala")
            return n+afturkvaem_summa_oddatala(n-1)
        else:
            return afturkvaem_summa_oddatala(n-1) #Þetta er slétt tala náðu í næstu tölu

num = int(input("Sláðu inn tölu"))
if num < 0:
    print("Verður að vera plústala")
else:
    print("Summa talnanna er ", afturkvaem_summa_oddatala(num))

