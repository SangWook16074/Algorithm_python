import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
psum = [0 for _ in range(n + 1)]
r = [0 for _ in range(m)]

for i in range(1, n + 1):
    psum[i] = psum[i - 1] + arr[i - 1]
    r[psum[i] % m] += 1

ans = r[0]
for i in r:
    ans += i * (i-1) // 2
print(ans)
