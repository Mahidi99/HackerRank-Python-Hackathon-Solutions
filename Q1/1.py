from decimal import Decimal
def MissingNo(x):
        
	n = len(x)
	1<=len(x)<10**5
	total = (n + 1)*(n + 2)/2
	sum_of_x = sum(x) 
	return total - sum_of_x

x = [int(i) for i in input().split(",")]
missNo = MissingNo(x) 
print (Decimal(missNo).normalize()) 
