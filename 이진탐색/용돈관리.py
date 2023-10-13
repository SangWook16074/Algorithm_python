import sys
input = sys.stdin.readline

n, m = map(int, input().split())
day = list(int(input()) for _ in range(n))

start = min(day)
end = sum(day)
while start <= end:
    mid = (start + end) // 2
    money = mid
    cnt = 1
    for i in range(n):
        if day[i] > money:
            money = mid
            cnt += 1
        money -= day[i]
    
    if cnt > m or mid < max(day):
        start = mid + 1
    else:
        end = mid - 1
        result = mid
print(result)