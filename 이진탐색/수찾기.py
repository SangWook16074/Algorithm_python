import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return 1
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

n = int(input())
numbers = sorted(list(map(int, input().split())))
m = int(input())
targets = list(map(int, input().split()))
for t in targets:
    result = binary_search(numbers, t, 0, len(numbers)-1)
    print(result)

