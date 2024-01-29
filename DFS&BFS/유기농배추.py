# import sys
# sys.setrecursionlimit(100000)
# input = sys.stdin.readline

# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]


# def dfs(x, y):
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return False

#     if graph[x][y] == 1:
#         graph[x][y] = 0
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             dfs(nx, ny)
#         return True
#     return False


# t = int(input())
# for _ in range(t):
#     m, n, k = map(int, input().split())
#     graph = [[0 for _ in range(m)] for _ in range(n)]
#     for _ in range(k):
#         x, y = map(int, input().split())
#         graph[y][x] = 1

#     result = 0
#     for i in range(n):
#         for j in range(m):
#             if dfs(i, j) == True:
#                 result += 1
#     print(result)

import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, graph, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if visited[nx][ny]:
                continue

            if graph[nx][ny] == 1:
                visited[nx][ny] = True
                graph[nx][ny] = 0
                q.append((nx, ny))


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                result += 1
                bfs(i, j, graph, visited)
    print(result)
