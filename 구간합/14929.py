import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
psum = [0 for _ in range(n+1)]
for i in range(1, n+1):
    psum[i] = psum[i-1] + arr[i-1]
ans = 0
for i in range(1, n):
    ans += arr[i-1] * (psum[n] - psum[i])
print(ans)