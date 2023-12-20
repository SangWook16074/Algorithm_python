import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
psum = [0]
total = 0
for num in arr:
    total += num
    psum.append(total)

for _ in range(int(input())):
    i, j = map(int, input().split())
    print(psum[j]-psum[i-1])
