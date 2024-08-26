import sys
input = sys.stdin.readline

n = int(input())
apple = [list(map(int, input().split())) for _ in range(n)]
psum = [[0 for _ in range(n+1)] for _ in range(n+1)]
for x in range(1, n+1):
    for y in range(1, n+1):
        psum[x][y] = psum[x][y - 1] + psum[x - 1][y] - psum[x - 1][y - 1] + apple[x - 1][y - 1]

ans = -1000
for k in range(1, n+1):
    for x in range(1, n - k + 2):
        for y in range(1, n - k + 2):
            ans = max(ans, psum[x + k - 1][y + k - 1] - psum[x + k - 1][y - 1] - psum[x - 1][y + k - 1] + psum[x - 1][y - 1])
print(ans)
