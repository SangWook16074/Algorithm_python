import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))
ans = -10000
for i in range(n-k+1):
    ans = max(ans, sum(temp[i:i+k]))
print(ans)