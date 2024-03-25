binary = input().strip()  
decimal = 0  
for i in range(len(binary) - 1, -1, -1):
    decimal += int(binary[i]) * (2 ** (len(binary) - i - 1))

print(decimal)  
