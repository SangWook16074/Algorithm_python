import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
r, c, n = map(int, input().split())
bomb = []
graph = [list(input().rstrip()) for _ in range(r)]
for y in range(r):
    for x in range(c):
        if graph[y][x] == 'O':
            bomb.append((x, y))
if n == 1:
    for g in graph:
        print("".join(g))
else:
    result = []
    graph = [['O' for _ in range(c)] for _ in range(r)]
    result.append([['O' for _ in range(c)] for _ in range(r)])
    for b in bomb:
        x, y = b
        graph[y][x] = '.'
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= c or ny < 0 or ny >= r:
                continue
            
            if graph[ny][nx] == 'O':
                graph[ny][nx] = '.'
    bomb = []
    result.append(graph)
    result.append([['O' for _ in range(c)] for _ in range(r)])
    for y in range(r):
        for x in range(c):
            if graph[y][x] == 'O':
                bomb.append((x, y))
    graph = [['O' for _ in range(c)] for _ in range(r)]
    for b in bomb:
        x, y = b
        graph[y][x] = '.'
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= c or ny < 0 or ny >= r:
                continue
            
            if graph[ny][nx] == 'O':
                graph[ny][nx] = '.'
    result.append(graph)
    if n % 4 == 2:
        for g in result[0]:
            print("".join(g))
    elif n % 4 == 3:
        for g in result[1]:
            print("".join(g))
    elif n % 4 == 0:
        for g in result[2]:
            print("".join(g))
    elif n % 4 == 1:
        for g in result[3]:
            print("".join(g))