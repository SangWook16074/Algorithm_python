import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

'''
0 : 북, 1 : 동, 2 : 남, 3 : 서
'''

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
result = 0
while True:
    if graph[r][c] == 0:
        graph[r][c] = 2
        result += 1

    cnt = 0
    for i in range(4):
        if graph[r+dy[i]][c+dx[i]] != 0:
            cnt += 1
    
    if cnt == 4:
        if graph[r-dy[d]][c-dx[d]] == 1:
            break
        else:
            r, c = r-dy[d], c-dx[d]
    else:
        for i in range(4):
            d -= 1
            if d < 0:
                d = 3
            if graph[r+dy[d]][c+dx[d]] == 0:
                r, c, d = r+dy[d], c+dx[d], d
                break

print(result)
