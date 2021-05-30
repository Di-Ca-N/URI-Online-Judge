from itertools import combinations


qtd, *seq = [int(x) - 1 for x in input().split()]

while qtd != -1:
    invs = 0
    #print(seq)
    for i, elem in enumerate(seq):
        #print(i, elem)
        invs += max(0, elem - i)

    # for i, elem in enumerate(reversed(seq)):
    #     invs += max(0, elem - (qtd - i)) 
    print(invs)
    qtd, *seq = [int(x) - 1 for x in input().split()]
