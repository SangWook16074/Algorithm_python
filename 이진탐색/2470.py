import sys
input = sys.stdin.readline

n = int(input())
liquid = sorted(list(map(int, input().split())))
left_idx = 0
right_idx = n-1
value = liquid[left_idx] + liquid[right_idx]
result = [left_idx, right_idx]

while left_idx != right_idx:
    left, right = liquid[left_idx], liquid[right_idx]
    total = left + right

    if abs(total) < abs(value):
        value = total
        result = [left_idx, right_idx]
        

    if total < 0:
        left_idx += 1
    else:
        right_idx -= 1
print(liquid[result[0]], liquid[result[1]])