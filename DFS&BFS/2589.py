import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]
result = 0
for j in range(n):
    for i in range(m):
        if graph[j][i] == 'L': 
            visited = [[0 for _ in range(m)] for _ in range(n)]
            q = deque()
            q.append((i, j))
            visited[j][i] = 1
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    
                    if graph[ny][nx] == 'W':
                        continue
                        
                    if visited[ny][nx] == 0:
                        visited[ny][nx] = visited[y][x] + 1
                        q.append((nx, ny))
            for k in range(n):
                for l in range(m):
                    result = max(result, visited[k][l])
print(result-1)
