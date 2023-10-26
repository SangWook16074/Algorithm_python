import sys
input = sys.stdin.readline

s = input().rstrip()
t = list(input().rstrip())
for i in range(len(t)):
    if t[-1] == 'A':
        t.pop()
    else:
        t.pop()
        t.reverse()
    
    if ''.join(t) == s:
        print(1)
        exit()
print(0)

