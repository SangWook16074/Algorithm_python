import sys
from collections import deque
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
dice = [0 for _ in range(7)]
up, north, east, west, south, bottom = 1, 2, 3, 4, 5, 6
for c in command:
    # 명령수행이 가능한가
    if c == 1:
        nx, ny = x, y+1
    elif c == 2:
        nx, ny = x, y-1
    elif c == 3:
        nx, ny = x-1, y
    else:
        nx, ny = x+1, y

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    if c == 1:
        tmp = east
        east = up
        up = west
        west = bottom
        bottom = tmp
    elif c == 2:
        tmp = west
        west = up
        up = east
        east = bottom
        bottom = tmp
    elif c == 3:
        tmp = north
        north = up
        up = south
        south = bottom
        bottom = tmp
    else:
        tmp = south
        south = up
        up = north
        north = bottom
        bottom = tmp

    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[bottom]
    else:
        dice[bottom] = graph[nx][ny]
        graph[nx][ny] = 0

    x, y = nx, ny
    print(dice[up])
