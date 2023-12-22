import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())
photo = [list(map(int, input().split())) for _ in range(r)]
psum = [[0] for _ in range(r+1)]
for i in range(1, r+1):
    total = 0
    for j in range(c):
        total += photo[i-1][j]
        psum[i].append(total)

for _ in range(q):
    result = 0
    r1, c1, r2, c2 = map(int, input().split())
    for i in range(r1, r2+1):
        result += psum[i][c2] - psum[i][c1-1]
    print(result // ((r2-r1+1)*(c2-c1+1)))
