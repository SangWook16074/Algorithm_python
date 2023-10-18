nonSelfNumbers = [i+sum(map(int, str(i))) for i in range(1, 10001)]
for i in range(1, 10001):
    if i not in nonSelfNumbers:
        print(i)