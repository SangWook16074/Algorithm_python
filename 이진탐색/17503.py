import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
beers = sorted([list(map(int, input().split())) for _ in range(k)], key= lambda x : (-x[0], x[1]))
start = 1
end = 2**31
try:
    while start <= end:
        mid = (start + end) // 2
        total = 0
        cnt = 0
        for v, c in beers:
            if cnt == n:
                break

            if c <= mid:
                total += v
                cnt += 1
        
        if total < m or cnt < n:
            start = mid + 1
        else:
            result = mid
            end = mid - 1
    print(result)
except:
    print(-1)
