import sys
input = sys.stdin.readline

cnt = 1
while True:
    l, p, v = map(int, input().split())
    if l==p==v==0:
        break
    result = (v // p)*l
    v %= p
    if v > l:
        result += l
    else:
        result += v
    print("Case {}: {}".format(cnt, result))
    cnt += 1