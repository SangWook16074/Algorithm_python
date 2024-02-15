import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def check(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return True
    return False


def bfs(x, y):
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    ex.append((x, y))
    visited[x][y] = True
    graph[x][y] = 2
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                graph[nx][ny] = 2
                q.append((nx, ny))
                ex.append((nx, ny))


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0
while True:
    flag = False
    ex = []
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0 and check(x, y):
                bfs(x, y)

            if graph[x][y] == 1:
                flag = True
    if not flag:
        break

    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                cnt = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if graph[nx][ny] == 2:
                        cnt += 1
                        if cnt == 2:
                            graph[x][y] = 0
                            break

    for x, y in ex:
        graph[x][y] = 0

    result += 1
print(result)
