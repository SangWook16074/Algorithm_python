import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] += arr[i-1][j-1] + dp[i][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = 0
    for i in range(x1, x2+1):
        result += dp[i][y2] - dp[i][y1-1]
    print(result)
