import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, graph, visited):
    union = [[x, y]]
    total = graph[x][y]
    cnt = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if visited[nx][ny]:
                continue

            if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                q.append((nx, ny))
                visited[nx][ny] = True
                total += graph[nx][ny]
                cnt += 1
                union.append([nx, ny])

    if cnt == 1:
        return 0
    else:
        people = total // cnt
        for u in union:
            graph[u[0]][u[1]] = people
        return 1


answer = 0
while True:
    result = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                result += bfs(x, y, graph, visited)
    if result > 0:
        answer += 1
    else:
        break
print(answer)
