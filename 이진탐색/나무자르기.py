import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for t in trees:
        if t > mid:
            total += t - mid
    
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)