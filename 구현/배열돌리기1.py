import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for _ in range(r):
    min_w, min_h, max_w, max_h = 0, 0, m-1, n-1
    while True:
        tmp, prev = 0, arr[min_h][max_w]
        for x in range(max_w-1, min_w-1, -1):
            tmp = arr[min_h][x]
            arr[min_h][x] = prev
            prev = tmp
    

        for y in range(min_h+1, max_h+1):
            tmp = arr[y][min_w]
            arr[y][min_w] = prev
            prev = tmp
    

        for x in range(min_w+1, max_w+1):
            tmp = arr[max_h][x]
            arr[max_h][x] = prev
            prev = tmp
    

        for y in range(max_h-1, min_h-1, -1):
            tmp = arr[y][max_w]
            arr[y][max_w] = prev
            prev = tmp
        
        min_w += 1
        min_h += 1
        max_w -= 1
        max_h -= 1

        if min_w > max_w or min_h > max_h:
            break

for a in arr:
    print(*a)

