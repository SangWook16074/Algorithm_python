import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]
psum = [[[0, 0] for _ in range(m+1)] for _ in range(n+1)]
for x in range(n):
    for y in range(m):
        for z in range(2):
            psum[x+1][y+1][z] = psum[x+1][y][z] + \
                psum[x][y+1][z] - psum[x][y][z]
        if (x+y) % 2:
            if graph[x][y] == "B":
                psum[x+1][y+1][0] += 1
            elif graph[x][y] == "W":
                psum[x+1][y+1][1] += 1

        else:
            if graph[x][y] == "W":
                psum[x+1][y+1][0] += 1
            elif graph[x][y] == "B":
                psum[x+1][y+1][1] += 1
ans = 2000000
for x in range(1, n-k+2):
    for y in range(1, m-k+2):
        x1, y1, x2, y2 = x, y, x+k-1, y+k-1
        for i in range(2):
            result = psum[x2][y2][i] - psum[x2][y1-1][i] - \
                psum[x1-1][y2][i] + psum[x1-1][y1-1][i]
            ans = min(result, ans)
print(ans)
