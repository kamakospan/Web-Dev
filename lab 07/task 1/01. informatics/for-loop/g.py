def smallest_divisor(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return i
    return x

x = int(input().strip())
print(smallest_divisor(x))
