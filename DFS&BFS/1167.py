import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def dfs(node, weight):
    for c, w in graph[node]:
        total = weight + w
        if visited[c] == -1:
            visited[c] = total
            dfs(c, total)


v = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v):
    arr = list(map(int, input().split()))
    node = arr[0]
    for j in range(1, len(arr)-1, 2):
        n, w = arr[j], arr[j+1]
        graph[node].append((n, w))
visited = [-1 for _ in range(v+1)]
visited[1] = 0
dfs(1, 0)
start, tmp = 0, 0
for i in range(1, v+1):
    if visited[i] > tmp:
        start, tmp = i, visited[i]
visited = [-1 for _ in range(v+1)]
visited[start] = 0
dfs(start, 0)
print(max(visited))
