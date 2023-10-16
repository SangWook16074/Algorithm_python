import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y, graph):
    q = deque()
    q.append((x, y))
    while q:
        dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        dy = [1, 0, -1, 1, 0, -1, 1, 0, -1]
        x, y = q.popleft()
        for i in range(9):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((nx, ny))
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    result = 0
    for y in range(h):
        for x in range(w):
            if graph[y][x]:
                result += 1
                bfs(x, y, graph)
    print(result)