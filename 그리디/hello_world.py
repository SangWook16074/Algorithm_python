s = 'hello'
arr = list(s)
tmp = arr[2:4]
for i in range(2, 4):
    arr[i] = tmp[i]
print(arr)