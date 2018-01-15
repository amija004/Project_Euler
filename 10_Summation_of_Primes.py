newnumm = 11
lix = [2,3,5,7]
if(newnumm%2 == 0):
	newnumm +=1
while(newnumm<2000000):
	counter = 3
	x = newnumm
	while(counter*counter <= newnumm):
		if (newnumm%counter == 0):
			newnumm += 2
		else:
			counter += 2
	if(x==newnumm):
		lix.append(newnumm)
		newnumm += 2
print("Sum of all primes less than 2 Million is ", sum(lix))
