import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
psum = [0 for _ in range(n+1)]
for i in range(1, n+1):
    psum[i] = psum[i - 1]
    if arr[i - 1] == 2:
        psum[i] -= 1
    else:
        psum[i] += 1


minIdx, maxIdx = 0, 0
minV, maxV = 100001, -100001
for i in range(n+1):
    curr = psum[i]
    if minV > curr:
        minIdx = i
        minV = curr
    
    if maxV < curr:
        maxIdx = i
        maxV = curr

print(abs(psum[maxIdx] - psum[minIdx]))
