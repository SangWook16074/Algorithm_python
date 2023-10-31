import sys
input = sys.stdin.readline

while True:
    n, a, b = map(int, input().split())
    if n == a == b == 0:
        break
    else:
        result = 0
        info = sorted([list(map(int, input().split())) for _ in range(n)], key= lambda x : -abs(x[1]-x[2]))
        for i in info:
            balloon, dis_a, dis_b = i[0], i[1], i[2]
            if dis_a > dis_b:
                if b >= balloon:
                    b -= balloon
                    result += dis_b*balloon
                else:
                    result += dis_b * b + dis_a * (balloon - b)
                    a -= (balloon - b)
                    b = 0
            elif dis_b > dis_a:
                if a >= balloon:
                    a -= balloon
                    result += dis_a * balloon
                else:
                    result += dis_a * a + dis_b * (balloon - a)
                    b -= (balloon - a)
                    a = 0
            else:
                result += dis_a * balloon
        print(result)