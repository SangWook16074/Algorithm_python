import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
result = 0
history = set()


def dfs(x, y, cnt):
    global result
    result = max(result, cnt)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in history:
            history.add(graph[nx][ny])
            dfs(nx, ny, cnt+1)
            history.remove(graph[nx][ny])


r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
history.add(graph[0][0])
dfs(0, 0, 1)
print(result)
