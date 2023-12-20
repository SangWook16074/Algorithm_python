import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
psum = [[0] for _ in range(n+1)]
for i in range(1, n+1):
    total = 0
    for num in arr[i-1]:
        total += num
        psum[i].append(total)

for _ in range(int(input())):
    result = 0
    i, j, x, y = map(int, input().split())
    for a in range(i, x+1):
        result += psum[a][y] - psum[a][j-1]
    print(result)
