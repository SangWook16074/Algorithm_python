import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
psum_dict = {0: 1}
total = 0
ans = 0
for a in arr:
    total += a
    if total - k in psum_dict.keys():
        ans += psum_dict[total - k]
    
    if total in psum_dict.keys():
        psum_dict[total] += 1
    else:
        psum_dict[total] = 1

print(ans)