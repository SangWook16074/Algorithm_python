import sys
input = sys.stdin.readline

n = int(input())
cards = [0] + list(map(int, input().split()))
dp = [0]*1001
dp[1] = cards[1]
dp[2] = max(cards[2], dp[1]+cards[1])
for i in range(3, n+1):
    dp[i] = cards[i]
    for j in range(1, i):
        dp[i] = max(dp[j]+cards[i-j], dp[i])
print(dp[n])