import sys
input = sys.stdin.readline

word = input().replace(' ','')
answer = 'UCPC'
idx = 0
for w in word:
    if w == answer[idx]:
        idx+=1
    
    if idx == 4:
        print('I love UCPC')
        exit()
print('I hate UCPC')