T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
 
A = [1,1]
for test_case in range(1, T + 1):
    n = int(input())
     
    for i in range(len(A), n+1):
        cand = []
        for k in range(1, i//2+1):
            cand.append(2*A[i-k] - A[(-2)*k+i])
             
        answer = 1
        while True:
            if answer in cand:
                answer += 1
            else:
                A.append(answer)
                break
                 
    print(A[n])
                