

n = input()  # 입력 받기
r1 = int(n[1]) # 뒷 숫자 받기
r2 = ord(n[0])-ord('a')+1 # 앞 문자 아스키코드로 변환 후 1로 변환

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
count =0
for c,d in steps: # steps를 c와 d로 나누어서 변수를 받는다
    dx=r2+c 
    dy=r1+d  
    if 0< dx <=8  and 0<dy<=8: # 조건 계산 8x8에 벗어나면 안된다
        count+=1

print(count)



