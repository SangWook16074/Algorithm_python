import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cctv = [()]
direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]],
    [[0, 1, 2, 3]]
]
result = 0
for x in range(n):
    for y in range(m):
        if graph[x][y] != 0 and graph[x][y] != 6:
            cctv.append((x, y, graph[x][y]))

        if graph[x][y] == 0:
            result += 1


def move(x, y, direction, copy):
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or copy[nx][ny] == 6:
                break

            if copy[nx][ny] != 0:
                continue

            copy[nx][ny] = "#"


def back(level, graph):
    global result
    copy = [[j for j in graph[i]] for i in range(n)]
    if level == len(cctv):
        cnt = 0
        for x in range(n):
            for y in range(m):
                if graph[x][y] == 0:
                    cnt += 1
        result = min(result, cnt)
        for x in range(n):
            for y in range(m):
                if graph[x][y] == "#":
                    graph[x][y] = 0
        return

    nx, ny, num = cctv[level]
    for d in direction[num]:
        move(nx, ny, d, copy)
        back(level + 1, copy)
        copy = [[j for j in graph[i]] for i in range(n)]


back(1, graph)
print(result)
