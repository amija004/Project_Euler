numm = 13
newnumm = 15
rank = 6

while(rank <= 10002):
	counter = 3
	x = newnumm
	if(newnumm%2 == 0):
		newnumm +=1
	while(counter*counter <= newnumm):
		if (newnumm%counter == 0):
			newnumm += 1
		else:
			counter += 2
	if(x == newnumm):
		numm = newnumm
		rank += 1
		newnumm += 2
	if(rank == 10001):
		print(numm, rank)
