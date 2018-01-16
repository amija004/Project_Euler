def istrip(a,b,c):
	if(a*a + b*b == c*c and a+b+c==1000):
		print("Batting 1.000 ", a*b*c, a, b, c)
		x=True

a = 1
b = 1
c = 2
x = False

while(x==False):
	print("A = ", a, "B = ", b, "C = ", c)
	for c in range(2,1000,1):
		istrip(a,b,c)
		for b in range(1,1000,1):
			istrip(a,b,c)
			for a in range(1,1000,1):
				istrip(a,b,c)
        
"""While this solution works, a better solution would be preferable,
possible based on the following:

the following math provided by Pier, https://projecteuler.net/thread=9
Without programming: 

a= 2mn; b= m^2 -n^2; c= m^2 + n^2; 
a + b + c = 1000; 

2mn + (m^2 -n^2) + (m^2 + n^2) = 1000; 
2mn + 2m^2 = 1000; 
2m(m+n) = 1000; 
m(m+n) = 500; 

m>n; 
m= 20; n= 5;
 
a= 200; b= 375; c= 425;"""
