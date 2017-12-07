try:
    while True:
        boots = []
        cont = 0
        a = int(input())
        for i in range(a):
            j = input().split()
            k = [j[0],"E" if j[1]=="D" else "D"]
            if k in boots:
                boots.remove(k)
                cont += 1
            else:
                boots.append(j)
        print(cont)

except EOFError:
    pass
