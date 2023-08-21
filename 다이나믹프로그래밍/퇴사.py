import sys
input = sys.stdin.readline
arr = [[] for i in range(20)]
n = int(input())
for i in range(1, n+1):
    t, p = map(int, input().split())
    # 끝나는날
    e = i + t - 1
    arr[e].append([t, p, i])
dp = [0]*16
for i in range(1, n+1):
    dp[i] = dp[i-1]
    if len(arr[i]) != 0:
        print(arr[i])
        for j in arr[i]:
            dp[i] = max(dp[i], j[1]+dp[j[2]-1])
print(dp[n])