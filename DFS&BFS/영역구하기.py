import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, graph):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    graph[y][x] = 0
    s = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                s += 1
                q.append((nx, ny))
    return s

m, n, k = map(int, input().split())
graph = [[1 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[y][x] = 0

result = []
for y in range(m):
    for x in range(n):
        if graph[y][x] == 1:
            result.append(bfs(x, y, graph))

result = sorted(result)
print(len(result))
print(*result)