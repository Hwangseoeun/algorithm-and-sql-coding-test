def calculateNum(reverseA, reverseB):
    for i in range(3):
        if reverseA[i] > reverseB[i]:
            return reverseA
        elif reverseA[i] < reverseB[i]:
            return reverseB
        else:
            continue

A, B = map(str, input().split(" "))

reverseA = list(A)
reverseA.reverse()

reverseB = list(B)
reverseB.reverse()

result = calculateNum(reverseA, reverseB)

for i in range(3):
    print(result[i], end="")

print()