def hanoi(n, X, Y, Z):
	if n == 1:
		print("Færum %s frá  %s til %s" %(n, X, Y))
		
	else:
		hanoi(n-1, X, Z, Y)
		print("Færum %s frá  %s til %s" %(n, X, Y))
		hanoi(n-1,Z,Y,X)

hanoi(3, "A", "B", "C")

#Færum 1 frá  A til B
#Færum 2 frá  A til C
#Færum 1 frá  B til C
#Færum 3 frá  A til B
#Færum 1 frá  C til A
#Færum 2 frá  C til B
#Færum 1 frá  A til B
# svar við 2: 2^n -1
