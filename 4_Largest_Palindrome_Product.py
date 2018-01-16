x=999
y=999
a = 0
for x in range(1000, 99, -1):
	for y in range(1000, 99, -1):
		z=x*y
		if(str(z) == str(z)[::-1]):
			if(z > a):
				a = z
print(a)
