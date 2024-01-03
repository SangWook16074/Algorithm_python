import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 배열을 순회하면서
# 테트로미노를 놓고
# 합을 구해서 비교
visited = [[False for _ in range(m)] for _ in range(n)]
cases = [
    # ㅗ 모양
    [[0, 1], [0, -1], [1, 0]],
    [[1, 0], [-1, 0], [0, 1]],
    [[0, 1], [0, -1], [-1, 0]],
    [[1, 0], [-1, 0], [0, -1]],
]
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
ans = 0


def dfs(x, y, cnt, total):
    global ans
    if cnt == 4:
        ans = max(ans, total)
        return
    for i in range(4):
        nx, ny = x + move[i][0], y + move[i][1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt+1, total+graph[nx][ny])
            visited[nx][ny] = False


def etc(x, y):
    global ans
    for case in cases:
        flag = False
        total = graph[x][y]
        for c in case:
            nx, ny = x+c[0], y+c[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                flag = True
                continue
            total += graph[nx][ny]
        if not flag:
            ans = max(ans, total)


for x in range(n):
    for y in range(m):
        visited[x][y] = True
        dfs(x, y, 1, graph[x][y])
        visited[x][y] = False
        etc(x, y)
print(ans)
