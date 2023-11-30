import sys
import math
input = sys.stdin.readline
n, m = map(int, input().split())
jewels = sorted([int(input()) for _ in range(m)], reverse=True)
start = 1
end = max(jewels)
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for jewel in jewels:
        cnt += math.ceil((jewel / mid))

    if cnt > n:
        start = mid + 1
    else:
        result = mid
        end = mid - 1
print(result)