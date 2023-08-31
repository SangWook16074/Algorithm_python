import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

start = 0
end = m

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in arr:
        if x <= mid:
            total += x
        else:
            total += mid
    
    if total > m:
        end = mid - 1
    else:
        result = max(arr) if max(arr) < mid else mid
        start = mid + 1
print(result)