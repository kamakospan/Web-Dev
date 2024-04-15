v = float(input())
t = float(input())

s = v * t 

if v < 0: 
    otmetka = int(109+s)
elif v > 0: 
    otmetka = int(s - 109)

print(otmetka)