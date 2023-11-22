import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 0 : 북, 1 : 동, 2 : 남, 3 : 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
result = 0
while True:
    if graph[r][c] == 0:
        graph[r][c] = 2
        result += 1

    # 주변 칸의 청소상태 스캔
    cnt = 0
    for i in range(4):
        if graph[r+dy[i]][c+dx[i]] != 0:
            cnt += 1
    
    # 청소할 수 없다면
    if cnt == 4:
        nr, nc = r-dy[d], c-dx[d]
        # 벽이라면 종료
        if graph[nr][nc] == 1:
            break
        # 후진 가능하면 이동
        else:
            r, c = nr, nc
    
    # 청소할 수 있다면
    else:
        # 반시계 방향으로 회전
        for i in range(4):
            d -= 1
            if d < 0:
                d = 3
            # 청소해야 하는 칸이 등장하면 이동 후 회전 종료
            nr, nc = r+dy[d], c+dx[d]
            if graph[nr][nc] == 0:
                r, c = nr, nc
                break
print(result)
