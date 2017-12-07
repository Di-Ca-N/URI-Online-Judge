#import pdb
#pdb.set_trace()

ops = {4: 3000, 3: 500, 2: 50}

valores = input().split()
while valores != ['0', '0', '0']:
    premio = False
    aposta = float(valores[0])
    numero_escolhido = valores[1].zfill(4)[-4:]
    numero_sorteado = valores[2].zfill(4)[-4:]
    grupo_escolhido = (int(numero_escolhido[-2:]) - int(numero_escolhido[-2:]) % 4) / 4
    grupo_sorteado = (int(numero_sorteado[-2:]) - int(numero_sorteado[-2:]) % 4) / 4

    if int(numero_sorteado) % 4 == 0:
        grupo_sorteado -= 1
    if int(numero_escolhido) % 4 == 0:
        grupo_escolhido -= 1

    if grupo_sorteado == grupo_escolhido:
        premio = aposta*16
    for teste in range(4, 1, -1):
        if numero_escolhido[-teste:] == numero_sorteado[-teste:]:
            k = teste
            break

    try:
        premio = aposta*ops[k]
        del k
    except NameError:
        if not premio:
            premio = 0

    print("{:.2f}".format(premio))
    valores = input().split()
