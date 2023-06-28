def solution(arr):
    stk = [arr[0]]
    i = 1
    while i < len(arr):
        if stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        else:
            stk.pop()
    return stk

print(solution([1, 4, 2, 5, 3, 8, 10]))