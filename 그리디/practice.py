import sys
input = sys.stdin.readline

units = []

n = int(input())
for _ in range(n):
	units.append(input().rstrip())

k = int(input())
for _ in range(k):
    result = input().rstrip()
    u = {}
    for unit in units:
        if unit.startswith(result):
            if unit not in u:
                u[unit] = 1
            else:
                u[unit] += 1
    
    if len(u) > 0:
        max_key = max(u, key=u.get) 
        print(max_key, u[max_key])
    else:
        print(0)