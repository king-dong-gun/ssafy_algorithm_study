import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, hex_num = input().split()

    result = ''

    for ch in hex_num:
        num = int(ch, 16)
        result += format(num, '04b')

    print(f'#{tc} {result}')