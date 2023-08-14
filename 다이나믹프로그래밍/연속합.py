import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * 100000
dp[0] = arr[0]
result = arr[0]
for i in range(1, n):
    dp[i] = max(dp[i-1]+arr[i], arr[i])
    result = max(dp[i], result)
print(result)
