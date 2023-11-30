import sys
input = sys.stdin.readline

n, k = map(int, input().split())
character = sorted([int(input()) for _ in range(n)])
start = 0
end = max(character)+k
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for c in character:
        if c < mid:
            cnt += mid - c
    
    # cnt가 k보다 모자르면
    if cnt > k:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)