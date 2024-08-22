import sys
import math
input = sys.stdin.readline

psum = [[0 for _ in range(1002)] for _ in range(1002)]
for x in range(1002):
    for y in range(1002):
        if x == y == 1:
            pass
        if x == 1 or y == 1:
            psum[x][y] += 1

for x in range(1, 1002):
    for y in range(1, 1002):
        psum[x][y] = psum[x-1][y] + psum[x][y-1] - psum[x-1][y-1]

        if math.gcd(x-1, y-1) == 1:
            psum[x][y] += 1

for _ in range(int(input())):
    n = int(input())
    print(psum[n+1][n+1])