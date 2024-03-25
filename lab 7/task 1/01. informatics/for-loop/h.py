def divisors(x):
    divisors_list = []
    for i in range (1, x+1):
        if x % i == 0:
            divisors_list.append(i)
    return divisors_list

a = int(input())

for j in divisors(a):
    print (j, end=" ")
