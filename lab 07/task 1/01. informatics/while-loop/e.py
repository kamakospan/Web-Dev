n = int(input())
k = 0
powOf2 = 1

while powOf2 < n:
    powOf2 *= 2
    k += 1

print(k)