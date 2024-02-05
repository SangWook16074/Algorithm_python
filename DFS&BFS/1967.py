import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def dfs(node, weight):
    for x, w in graph[node]:
        total = weight + w
        if visited[x] == -1:
            visited[x] = total
            dfs(x, total)


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))
    graph[c].append((p, w))
visited = [-1 for _ in range(n+1)]
visited[1] = 0
dfs(1, 0)
start, tmp = 0, 0
for i in range(1, n+1):
    if visited[i] > tmp:
        start, tmp = i, visited[i]
visited = [-1 for _ in range(n+1)]
visited[start] = 0
dfs(start, 0)
print(max(visited))
