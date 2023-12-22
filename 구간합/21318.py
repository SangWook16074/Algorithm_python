import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
psum = [0]
total = 0
for i in range(n-1):
    if arr[i+1] < arr[i]:
        total += 1
    psum.append(total)
for _ in range(int(input())):
    x, y = map(int, input().split())
    print(psum[y-1]-psum[x-1])
