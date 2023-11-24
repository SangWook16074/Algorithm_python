import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
for x in range(m):
    for y in range(n):
        for z in range(h):
            if graph[z][y][x] == 1:
                q.append((x, y, z))

while q:
    x, y, z = q.popleft()
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h:
            continue

        if graph[nz][ny][nx] == 0:
            graph[nz][ny][nx] = graph[z][y][x] + 1
            q.append((nx, ny, nz))

result = 0
for x in range(m):
    for y in range(n):
        for z in range(h):
            if graph[z][y][x] == 0:
                print(-1)
                exit()
            result = max(result, graph[z][y][x])
print(result-1)