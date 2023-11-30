import sys
input = sys.stdin.readline

n = int(input())
words = [input().split() for _ in range(n)]
short_cut = []
complete = []
for word in words:
    option = " ".join(word)
    flag = False
    for i in range(len(word)):
        if option in complete:
            continue
        
        if word[i][0].upper() not in short_cut and word[i][0].lower() not in short_cut:
            flag = True
            short_cut.append(word[i][0])
            complete.append(option)
            word[i] = "["+word[i][0]+"]"+word[i][1:]
            print(" ".join(word))
            break
    
    for i in range(len(option)):
        if option in complete:
            continue

        if option[i] == " ":
            continue

        if option[i].upper() not in short_cut and option[i].lower() not in short_cut:
            flag = True
            short_cut.append(option[i])
            complete.append(option)
            result = option[:i]+"["+option[i]+"]"+option[i+1:]
            print("".join(result))
            break
    if not flag:
        print(option)