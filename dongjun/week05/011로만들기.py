x = int(input())
arr = [0]*30001
for i in range(2, x+1):
    arr[i] = arr[i-1]+1
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i//2]+1)
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i//3]+1)
    if i % 5 == 0:
        arr[i] = min(arr[i], arr[i//5]+1)
print(arr[x])