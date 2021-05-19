total_sum = 0
n, m, l = map(int, input().split())

for i in range(1, l+1):
    if (i % n == 0 or i % m == 0):
        total_sum+=i
print (total_sum)  
