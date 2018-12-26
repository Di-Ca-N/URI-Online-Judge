n = int(input())

for i in range(n):
    valores = input().split()
    p_a, p_b, g_a, g_b = int(valores[0]), int(valores[1]), float(valores[2]), float(valores[3])
    taxa_a = g_a/100
    taxa_b = g_b/100

    for ano in range(1, 102):
        p_a += int(p_a * taxa_a)
        p_b += int(p_b * taxa_b)

        if p_a > p_b and ano <= 100:
            print("{} anos.".format(ano))
            break

    if ano == 101:
        print("Mais de 1 seculo.")
