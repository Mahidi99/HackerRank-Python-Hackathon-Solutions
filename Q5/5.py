from math import gcd 
def SimplifyFraction(a, b) : 
	frac = gcd(a, b); 
	a = a // frac; 
	b = b // frac;
	print(a,b,sep='/',end='\n')
 
if __name__ == "__main__" : 
        a, b = map(int, input().split("/"))
        SimplifyFraction(a,b)


