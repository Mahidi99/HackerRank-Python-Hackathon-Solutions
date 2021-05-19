total = 0
list1 = [1,1,1,2,2,3,4,5,7,9,12,16,21,28,37,49,65,86,114,151,200,265] 
n = int(input("num : "))
for i in range(0, len(n)): 
	total = total + list1[n] 
    
print("Sum of all elements in given list: ", total) 
