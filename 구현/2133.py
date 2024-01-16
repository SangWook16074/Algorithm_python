import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(31)]
dp[2] = 3
if n % 2 == 1:
    print(0)
else:
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2]*dp[2]+sum(dp[:i-2])*2+2
    print(dp[n])
