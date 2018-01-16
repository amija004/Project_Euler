z=0
x=1
y=1
w=0
a=0
for x in range(0,101):
	print(x)
	z += x*x
	x += 1
for y in range(0,101):
	print(y)
	w += y
	y += 1
	if y > 100:
		a = w*w
if z>a:
	print(z-a)
if a>z:
	print(a-z)
