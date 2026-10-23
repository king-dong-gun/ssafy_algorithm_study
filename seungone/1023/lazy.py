def main():
    def rd():
        s = input().split()
        while not s:
            s = input().split()
        return s
    tc = int(rd()[0])
    out = []
    for _ in range(tc):
        n = int(rd()[0])
        T = [0] * n
        D = [0] * n
        for i in range(n):
            s = rd()
            T[i] = int(s[0])
            D[i] = int(s[1])
        order = sorted(range(n), key=D.__getitem__, reverse=True)
        cur = 1 << 62
        for i in order:
            d = D[i]
            if d < cur:
                cur = d
            cur -= T[i]
        out.append(str(cur))
    print('\n'.join(out))
 
main()