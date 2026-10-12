def calc(nums, facs):
    result = nums[0]
    for i in range(N-1):
        if facs[i] == 0:
            result += nums[i+1]
        elif facs[i] == 1:
            result -= nums[i+1]
        elif facs[i] == 2:
            result *= nums[i+1]
        else:
            if result < 0:
                result = -((-result) // nums[i+1])
            else:
                result //= nums[i+1]
    return result

def go(depth):
    global mincal, maxcal
    if depth == N-1:
        temp = calc(nums, path)
        if mincal > temp:
            mincal = temp
        if maxcal < temp:
            maxcal = temp
        return
    
    for i in range(4):
        if factors[i]:
            factors[i] -= 1
            path.append(i)
            go(depth+1)
            factors[i] += 1
            path.pop()
            
            
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    factors = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    mincal = float('inf')
    maxcal = -float('inf')
    path = []
    go(0)
    print(f'#{tc} {maxcal-mincal}')
    
    
"""
2
5
2 1 0 1
3 5 3 7 9
6
4 1 0 0
1 2 3 4 5 6

변형 중복순열문제
길이 4짜리 연산자 배열을 만들어서
visited 대신 사용 (0이면 visited == True 랑 같은 효과)

"""
