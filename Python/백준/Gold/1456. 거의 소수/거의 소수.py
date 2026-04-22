A, B = map(int, input().split())

decimal = [True] * (int(B ** 0.5) + 1)
decimal[0] = False
decimal[1] = False

for i in range(2, int(B ** 0.5) + 1):
    if decimal[i]:
        for j in range(i * 2, int(B ** 0.5) + 1, i):
            decimal[j] = False

count = 0

for i in range(2, int(B ** (0.5)) + 1):
    step = 2
    current = i ** step
    
    if decimal[i]:
        while current <= B:
            if current >= A: 
                count += 1
            
            step += 1
            current = i ** step

print(count)