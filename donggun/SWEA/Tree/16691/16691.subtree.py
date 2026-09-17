import sys
sys.stdin = open("sample_input.txt", "r")

def pre_order(T):           # 전위 순회
    global count
    if T:                   # 0 이 아니라면 (존재하는 정점이면)
        count += 1          # T에서 할 일 처리
        pre_order(left[T])
        pre_order(right[T])


T = int(input())

for test_case in range(1, T + 1):
    # 간선의 개수 E, 서브트리 루트 N
    E, N = map(int, input().split())

    # 노드 개수 = 간선 개수 + 1
    V = E + 1   # 마지막 정점 번호
    tree = list(map(int, input().split()))

    # 부모를 인덱스로 자식번호 저장
    left = [0] * (V + 1)
    right = [0] * (V + 1)

    for i in range(E):
        parent, child = tree[i * 2], tree[i * 2 + 1]
        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    count = 0
    pre_order(N)
    print(f"#{test_case} {count}")
