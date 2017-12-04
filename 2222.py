
n = int(input())

for i in range(n):
    m = int(input())
    conj = {}
    for j in range(m):
        p = set(input().split()[1:])
        conj[j+1] = p
    o = int(input())
    for k in range(o):
        op, conj1, conj2 = input().split()
        if op == "1":
            elementos = conj[int(conj1)].intersection(conj[int(conj2)])

        else:
            elementos = conj[int(conj1)].union(conj[int(conj2)])

        print(len(elementos))
