import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    money = [0] + list(map(int, input().split()))
    m = int(input())
    dp = [[0 for _ in range(10001)] for _ in range(21)]
    for i in range(1, n+1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j]
            if dp[i][j-money[i]] > 0:
                dp[i][j] += dp[i][j-money[i]]
    
    print(dp[n][m])