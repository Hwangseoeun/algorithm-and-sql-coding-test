N = list(map(int, input().strip()))

for i in range(len(N)):
    max = i
    for j in range(i+1, len(N)):
        if N[j] > N[max]:
            max = j

    if N[i] < N[max]:
        N[i], N[max] = N[max], N[i]

for i in range(len(N)):
    print(N[i], end="")
print()