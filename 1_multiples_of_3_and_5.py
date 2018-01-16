lix = []
liy = []
liz = []
for x in range(0, 1000, 3):
	lix.append(x)
for y in range(0, 1000, 5):
	liy.append(y)
for z in range(0, 1000, 15):
	liz.append(z)
print(sum(liy) + sum(lix) - sum(liz))
