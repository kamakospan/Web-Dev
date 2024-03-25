def smallest_divisor(x):
    divisor = 2  
    while divisor <= x:
        if x % divisor == 0:  
            return divisor
        divisor += 1  

x = int(input().strip())
print(smallest_divisor(x))
