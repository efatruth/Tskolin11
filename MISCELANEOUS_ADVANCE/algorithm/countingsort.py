def countingSort():
	y = 0
	listi = [4,7,2,4,1,3,5]
	newList = []
	for x in listi:
		y = y + x
		newList.append(y)
	for x in listi:
		number = newListi[x]
		newList[number] = x - 1
	return newList
