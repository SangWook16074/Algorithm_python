import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
time = 0
shark_size = 2
eat = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark = [i, j]


def bfs(x, y, graph):
    result = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[0 for _ in range(n)] for _ in range(n)]

    q = deque()
    visited[x][y] = 0
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] > shark_size:
                continue

            if visited[nx][ny]:
                continue

            if graph[nx][ny] == 9:
                continue

            if graph[nx][ny] <= shark_size:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                if 0 < graph[nx][ny] < shark_size:
                    result.append([nx, ny, visited[nx][ny]])
    result = sorted(result, key=lambda x: (x[2], x[0], x[1]))
    return result[0] if len(result) != 0 else [0, 0, 0]


while True:
    rx, ry, distance = bfs(shark[0], shark[1], graph)
    if rx == ry == distance == 0:
        break
    graph[shark[0]][shark[1]] = 0
    graph[rx][ry] = 9
    shark = [rx, ry]
    time += distance
    eat += 1
    if eat == shark_size:
        shark_size += 1
        eat = 0
print(time)
