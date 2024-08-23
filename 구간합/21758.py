import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
psum = [0 for _ in range(n+1)]
for i in range(1, n+1):
    psum[i] = psum[i-1] + arr[i-1]
ans = 0
for i in range(2, n):
    ans = max(ans, 2 * psum[n] - psum[1] - psum[i] - arr[i-1])

for i in range(2, n):
    ans = max(ans, psum[n-1] + psum[i-1] - arr[i-1])

for i in range(2, n):
    ans = max(ans, psum[i] - psum[1] + psum[n-1] - psum[i-1])

print(ans)