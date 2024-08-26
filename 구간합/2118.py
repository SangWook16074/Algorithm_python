import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
psum = [0 for _ in range(n + 1)]
for i in range(1, n+1):
    psum[i] = psum[i - 1] + arr[i - 1]

ans = 0
start, end = 1, 1
while start <= end and end < n+1:
    right_way = psum[end] - psum[start - 1]
    left_way = psum[n] - psum[end] + psum[start - 1]

    if right_way - left_way < 0:
        ans = max(ans, right_way)
        end += 1
    else:
        ans = max(ans, left_way)
        start += 1
print(ans)
