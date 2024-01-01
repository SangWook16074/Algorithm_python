import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
wall = []
virus = []
result = 0


def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))


# 벽을 세우고
for x in range(n):
    for y in range(m):
        if graph[x][y] == 0:
            wall.append([x, y])
        elif graph[x][y] == 2:
            virus.append([x, y])
l = len(wall)
for i in range(l):
    for j in range(i+1, l):
        for k in range(j+1, l):
            cnt = 0
            visited = [
                [0 if graph[x][y] == 0 else 1 for y in range(m)] for x in range(n)]
            # 벽을 세우고
            visited[wall[i][0]][wall[i][1]] = 9
            visited[wall[j][0]][wall[j][1]] = 9
            visited[wall[k][0]][wall[k][1]] = 9
            # bfs()
            for v in virus:
                bfs(v[0], v[1], visited=visited)
            # 안전영역 세기
            for x in range(n):
                for y in range(m):
                    if visited[x][y] == 0:
                        cnt += 1
            result = max(result, cnt)
print(result)
