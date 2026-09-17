import sys
sys.stdin = open("sample_input(1).txt", "r")

def bst(n):
    if n <= N:
        global count
        bst(n * 2)
        count += 1
        tree[n] = count
        bst(n * 2 + 1)


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)        # 노드번호를 인덱스로 사용해서 저장
    count = 0
    bst(1)                      # 완전이진트리 루트부터 중위순회

    print(f"#{test_case} {tree[1]} {tree[N // 2]}")