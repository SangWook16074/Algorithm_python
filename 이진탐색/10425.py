import sys
input = sys.stdin.readline

fibo = {}
dp = [0] * 100001
dp[1] = 1
for i in range(2, 100001):
    dp[i] = dp[i-1] + dp[i-2]
    fibo[dp[i]] = i
t = int(input())
for _ in range(t):
    f = int(input())
    if f == 1:
        print(2)
    else:
        print(fibo[f])
