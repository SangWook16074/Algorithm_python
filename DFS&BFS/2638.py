import sys
from collections import deque
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                return True

            if not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))
    return False


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0
while True:
    flag = False
    tmp = []
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                flag = True
                cnt = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if graph[nx][ny] == 0 and bfs(nx, ny):
                        cnt += 1
                        if cnt >= 2:
                            tmp.append((x, y))
                            break
    for x, y in tmp:
        graph[x][y] = 0

    if not flag:
        break
    else:
        result += 1

print(result)
