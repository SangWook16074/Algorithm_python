import sys
from collections import deque
input = sys.stdin.readline


dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
t = int(input())
for _ in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    if sx == ex and sy == ey:
        print(0)
    else:
        graph = [[0 for _ in range(l)] for _ in range(l)]
        q = deque()
        q.append((sx, sy))
        while q:
            x, y = q.popleft()
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= l or ny < 0 or ny >= l:
                    continue

                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    q.append((nx, ny))
        print(graph[ey][ex])

