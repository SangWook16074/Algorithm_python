import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memories = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(sum(costs)+1)] for _ in range(N+1)]
result = sum(costs)
for n in range(1, N+1):
    memory = memories[n]
    cost = costs[n]
    for c in range(1, sum(costs)+1):
        if c < cost:
            dp[n][c] = dp[n-1][c]
        else:
            dp[n][c] = max(dp[n-1][c-cost]+memory, dp[n-1][c])

        if dp[n][c] >= M:
            result = min(result, c)
print(result if M != 0 else 0)