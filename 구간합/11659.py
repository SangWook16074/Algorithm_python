import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
psum = [0 for _ in range(n+1)]

for i in range(1, n+1):
    psum[i] = arr[i-1] + psum[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(psum[j]-psum[i-1])
