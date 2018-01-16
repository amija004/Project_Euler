x1 = 1
x2 = 2
lix = [2]
for y in range (0, 10000):
	y = x1 + x2
	x1 = x2
	x2 = y
	"print(y)"
	if y%2 == 0 and y < 4000000:
		lix.append(y)
print(sum(lix))
