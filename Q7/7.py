def squares() : 
        sum = 0
        a, b = map(int, input().split())
        for i in range(a, b+1) :
                sum+=(i**2)
        return sum 
print(squares()) 
