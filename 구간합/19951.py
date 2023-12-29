import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heights = list(map(int, input().split()))
order = [0 for _ in range(n+1)]
for _ in range(m):
    a, b, k = map(int, input().split())
    order[a-1] += k
    order[b] -= k
change = 0
for i in range(n):
    change += order[i]
    heights[i] += change
print(*heights)
