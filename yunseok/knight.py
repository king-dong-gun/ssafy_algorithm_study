alpa, num = input()
step = [(2, 1), (2, -1), (-1, -2), (1,-2), (-2,-1), (-2, 1), (-1, 2), (1, 2),]
count = 0

alpa = ord(alpa)
num = int(num)

for i in range(len(step)):
    x = step[i][0]
    y = step[i][1]
    if 96 < (alpa + x) < 105 and 0 < (num + y) < 9:
        count += 1
    
print(count)
print(ord('a'))
print(ord('A'))
'''

alpa, num = input().strip()
step = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

col = ord(alpa.lower()) - ord('a')   # 0~7
row = int(num) - 1                   # 0~7

count = sum(1 for dx, dy in step
            if 0 <= col + dx < 8 and 0 <= row + dy < 8)
print(count)

'''