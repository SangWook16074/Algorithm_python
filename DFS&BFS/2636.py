import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def isAir(x, y):
    if graph[x][y] == 1:
        return False

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return True

        if graph[nx][ny] == 2:
            return True
    return False


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

time = 0
result = 0
while True:
    tmp = []
    cnt = 0
    for x in range(n):
        for y in range(m):
            if isAir(x, y):
                bfs(x, y)

    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                cnt += 1
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if graph[nx][ny] == 2:
                        tmp.append((x, y))
                        break

    for x, y in tmp:
        graph[x][y] = 2

    if cnt == 0:
        break
    else:
        time += 1
        result = cnt
print(time)
print(result)
