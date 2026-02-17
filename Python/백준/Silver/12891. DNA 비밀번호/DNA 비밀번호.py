S, P = map(int, input().split())
dna = list(input().strip())
aCheck, cCheck, gCheck, tCheck = map(int, input().split())

startIdx = 0
endIdx = P-1
count = 0
aCnt, cCnt, gCnt, tCnt = 0, 0, 0, 0

for i in range(P):
    if dna[i] == 'A':
        aCnt += 1
    elif dna[i] == 'C':
        cCnt += 1
    elif dna[i] == 'G':
        gCnt += 1
    elif dna[i] == 'T':
        tCnt += 1

while endIdx != S:
    if aCnt >= aCheck and cCnt >= cCheck and gCnt >= gCheck and tCnt >= tCheck:
        count += 1
    
    if dna[startIdx] == 'A':
        aCnt -= 1
    elif dna[startIdx] == 'C':
        cCnt -= 1
    elif dna[startIdx] == 'G':
        gCnt -= 1
    elif dna[startIdx] == 'T':
        tCnt -= 1
    
    startIdx += 1
    endIdx += 1
    
    if endIdx == S:
        break
    
    if dna[endIdx] == 'A':
        aCnt += 1
    elif dna[endIdx] == 'C':
        cCnt += 1
    elif dna[endIdx] == 'G':
        gCnt += 1
    elif dna[endIdx] == 'T':
        tCnt += 1

print(count)