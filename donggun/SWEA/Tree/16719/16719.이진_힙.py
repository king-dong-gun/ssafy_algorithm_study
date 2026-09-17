import sys
sys.stdin = open("sample_input(1).txt", "r")

def enq(n):
    global last_value
    last_value += 1         # 마지막 정점 추가
    heap[last_value] = n    # 마지막 정점에 저장

    # 최소 힙 = 부모 < 자식
    child = last_value
    parent = child // 2
    while parent > 0 and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        # 부모와 부모의 부모를 비교한다.
        child = parent
        parent = child // 2


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    heap = [0] * (N + 1)    # N개의 정점을 가진 완전 이진트리
    last_value = 0          # 마지막 정점 번호

    for i in arr:
        enq(i)

    # 마지막 노드의 부모부터 루트까지 올라가면서 합치기
    parent = last_value // 2
    sum_value = 0

    while parent > 0:
        sum_value += heap[parent]
        parent = parent // 2
    print(f"#{test_case} {sum_value}")
