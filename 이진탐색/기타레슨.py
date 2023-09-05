import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))

start = max(lectures)
end = start * n
if m == n:
    print(max(lectures))
else:
    while start <= end:
        mid = (start + end) // 2
        cnt = 1
        length = mid
        for l in lectures:
            if length < l:
                cnt += 1
                length = mid
            length -= l

        if cnt <= m:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    print(result)