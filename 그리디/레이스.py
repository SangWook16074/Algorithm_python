import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
position = list(map(int, input().split()))

start = 1
end = position[-1] - position[0]
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    prev = position[0]
    for i in range(1, k):
        if position[i] - prev >= mid:
            cnt += 1
            prev = position[i]
    
    if cnt < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
ans = '1'
cnt = 1
prev = position[0]
for i in range(1, k):
    if position[i] - prev >= result and cnt < m:
        ans += '1'
        cnt += 1
        prev = position[i]
    else:
        ans += '0'
print(ans)