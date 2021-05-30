disponivel = [int(x) for x in input().split()]
desejado = [int(x) for x in input().split()]

print(sum(max(w - h, 0) for h, w in zip(disponivel, desejado)))