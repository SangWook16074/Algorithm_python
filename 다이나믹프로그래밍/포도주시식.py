import sys
input = sys.stdin.readline

n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))
dp = [0] * 10001
if n >= 1:
    dp[1] = arr[1]

if n >= 2:
    dp[2] = arr[1]+arr[2]

if n >= 3:
    dp[3] = max(dp[2], arr[1]+arr[3], arr[2]+arr[3])

if n >= 4:
    dp[4] = max(dp[2]+arr[4], arr[2]+arr[3], arr[1]+arr[3]+arr[4])

if n >= 5:
    for i in range(5, n+1):
        dp[i] = max(dp[i-2]+arr[i], arr[i-2]+arr[i-1]+dp[i-4], dp[i-3]+arr[i-1]+arr[i])

print(dp[n])