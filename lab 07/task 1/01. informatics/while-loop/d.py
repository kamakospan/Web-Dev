n = int(input())
powOf2 = 1

while powOf2 < n:
    powOf2 *= 2

if powOf2 == n:
    print("YES")
else:
    print("NO")