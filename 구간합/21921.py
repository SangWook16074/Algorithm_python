import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visit = list(map(int, input().split()))
if max(visit) == 0:
    print("SAD")
else:
    psum = [0]
    total = 0
    for v in visit:
        total += v
        psum.append(total)

    visitor = []
    for i in range(n-x+1):
        visitor.append(psum[i+x]-psum[i])
    result = max(visitor)
    cnt = 0
    for v in visitor:
        if v == result:
            cnt += 1
    print(result)
    print(cnt)
