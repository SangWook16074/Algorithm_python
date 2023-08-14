import sys
input = sys.stdin.readline

n = int(input())
arr = [[]]
for _ in range(n):
    arr.append(list(map(int, input().split())))
if n == 1:
    print(arr[1][0])
else:
    dp = [[0]*i for i in range(n+1)]
    dp[1][0] = arr[1][0]
    dp[2][0] = arr[1][0]+arr[2][0]
    dp[2][1] = arr[1][0]+arr[2][1]
    for i in range(2, n):
        for j in range(i):
            for k in range(j, j+2):
                dp[i+1][k] = max(dp[i][j]+arr[i+1][k], dp[i+1][k])
    print(max(dp[n]))