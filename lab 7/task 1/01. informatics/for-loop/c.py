a = int(input())
b = int(input())

for x in range (a, b+1):
    sq = x * x 
    if sq >= a and sq <= b:
        print (sq, end = " ")
    else:
        continue