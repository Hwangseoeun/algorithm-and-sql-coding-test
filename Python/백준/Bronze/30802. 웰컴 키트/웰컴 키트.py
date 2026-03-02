N = int(input())
t = list(map(int, input().split()))
tBundle, penBundle = map(int, input().split())

tBundleCnt = 0
penBundleCnt = 0
penCnt = 0

for i in range(len(t)):
    if t[i] % tBundle > 0:
        tBundleCnt += t[i] // tBundle + 1
    else:
        tBundleCnt += t[i] // tBundle

penBundleCnt = N // penBundle
penCnt = N % penBundle

print(tBundleCnt)
print(penBundleCnt, penCnt)