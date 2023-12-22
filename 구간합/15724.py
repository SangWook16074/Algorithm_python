import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
psum = [[0] for _ in range(n+1)]
for i in range(1, n+1):
    total = 0
    for j in range(m):
        total += arr[i-1][j]
        psum[i].append(total)

for _ in range(int(input())):
    result = 0
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2+1):
        result += psum[i][y2] - psum[i][y1-1]
    print(result)
