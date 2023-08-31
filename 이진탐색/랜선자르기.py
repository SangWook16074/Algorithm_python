import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lans = []
for _ in range(k):
    lans.append(int(input()))

start = 0
end = max(lans)

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for l in lans:
        if mid == 0:
            cnt += l
        else:
            cnt += l // mid

    if cnt < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)