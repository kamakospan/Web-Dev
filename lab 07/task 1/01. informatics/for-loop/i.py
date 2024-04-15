import math

def div_cnt(x):
    count = 0
    sqrt_x = int(math.sqrt(x))
    for i in range(1, sqrt_x + 1):
        if x % i == 0:
            count += 1
            if i != x // i:
                count += 1
    return count

a = int(input())
print(div_cnt(a))
