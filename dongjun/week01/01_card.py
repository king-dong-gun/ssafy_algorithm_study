N, M = map(int, input().split()) 
cards = []
for row in range(N):
    row = list(map(int, input().split()))
    cards.append(row)
answer = 0
for rows in cards:
    rowsmall = sorted(rows, reverse=True).pop()
    if answer <= rowsmall:
        answer = rowsmall
print(answer)


"""
3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4
"""