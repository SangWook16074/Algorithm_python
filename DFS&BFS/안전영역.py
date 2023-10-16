import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, visited):
    q = deque()
    visited[y][x] = True
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((nx, ny))

n = int(input())
graph = []
start = 100
end = 1
for _ in range(n):
    arr = list(map(int, input().split()))
    start = min(start, min(arr))
    end = max(end, max(arr))
    graph.append(arr)

result = 0
for i in range(start, end+1):
    visited = [[False if graph[h][w] > i else True for w in range(n)] for h in range(n)]
    cnt = 0
    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                cnt += 1
                bfs(x, y, visited)
    result = max(result, cnt)
print(result if result > 0 else 1)

