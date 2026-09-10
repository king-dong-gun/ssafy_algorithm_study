n= int(input())

arr1 = list(map(int, input().split()))

m = int(input())

arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()
for i in arr2:
    if i in arr1:
        print("yes", end=" ")
    else:
        print("no", end=" ")
'''
5
8 3 7 9 2
3
5 7 9
'''
