import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = y * 100 // x
if z >= 99:
    print(-1)
else:
    result = 0
    start = 1
    end = x
    while start <= end:
        mid = (start + end) // 2
        win = y + mid
        total = x + mid
        win_rate = win * 100 // total
        if win_rate <= z:
            start = mid + 1
        else:
            result = mid
            end = mid - 1
    print(result)