import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, graph):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
    
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                q.append((nx, ny))

m, n = map(int, input().split())
graph = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(j, i, graph)

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit()
    result = max(result, max(graph[i]))
print(result - 1)