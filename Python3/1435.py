a = int(input())

while a != 0:
    saida  = []
    for k in range(a):
        saida.append([1]*a)
    for i in range(1, int(a/2)+1):
        for j in range(i, a-i):
            for k in range(i, a-i):
                saida[j][k] = i+1

    out = ' '.join(["%3s"]*a)
    for linha in saida:
        print(out%tuple(linha))
    print()
    a = int(input())
