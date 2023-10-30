import sys
input = sys.stdin.readline

l, k, c = map(int, input().split())
position = sorted(list(set([0, *list(map(int, input().split())), l])))
pieces = [position[i] - position[i-1] for i in range(1, len(position))]
start = 1
end = l

while start <= end:
    mid = (start + end) // 2

    if max(pieces) > mid:
        start = mid + 1
    else:
        total = 0
        cnt = 0
        for p in pieces[::-1]:
            total += p
            if total > mid:
                total = p
                cnt += 1
        if cnt > c:
            start = mid + 1
        else:
            ans_result = mid
            ans_front = total if cnt == c else pieces[0]
            end = mid - 1

print(ans_result, ans_front)