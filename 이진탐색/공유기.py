import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()
if c == 2:
    print(house[-1] - house[0])
else:
    start = 1
    end = house[-1] - house[0]
    while start <= end:
        cnt = 1
        mid = (start + end) // 2
        current = house[0]
        for i in range(1, len(house)):
            if house[i] - current >= mid:
                current = house[i]
                cnt += 1
        
        if cnt < c:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    print(result)