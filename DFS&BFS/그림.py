import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, graph):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    size = 1
    q = deque()
    q.append((x, y))
    graph[y][x] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = 0 
                size += 1
                q.append((nx, ny))
    return size
    

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
result = 0
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            cnt += 1
            result = max(result, bfs(x, y, graph))
print(cnt)
print(result)