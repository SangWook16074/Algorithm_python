import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

result = 1e9
for c in combinations(chicken, m):
    total = 0
    for hx, hy in house:
        min_distance = 1e9
        for cx, cy in c:
            min_distance = min(min_distance, abs(hx-cx)+abs(hy-cy))
        total += min_distance
    result = min(result, total)
print(result)