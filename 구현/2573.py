import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, visited):
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny] and graph[nx][ny] != 0:
                visited[nx][ny] = True
                q.append((nx, ny))


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0
while True:
    ice = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if not visited[x][y] and graph[x][y] != 0:
                ice += 1
                bfs(x, y, visited)

    if ice == 0:
        print(0)
        break

    elif ice >= 2:
        print(result)
        break

    tmp = []
    for x in range(n):
        for y in range(m):
            if graph[x][y] != 0:
                cnt = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                        cnt += 1
                tmp.append((x, y, cnt))

    for x, y, z in tmp:
        graph[x][y] -= z
        if graph[x][y] < 0:
            graph[x][y] = 0

    result += 1
