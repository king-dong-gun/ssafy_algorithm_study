m, n = map(int, input().split())

result = 0

for a in range (m):
    data = list(map(int, input().split()))
    value = 10000

    for j in range(n):
        if data[j] < value:
            value = data[j]
    if result < value:
        result = value

print(result)