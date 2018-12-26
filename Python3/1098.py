i, j = 0, 1

for a in range(11):
    if (int(i) == i) and (int(j) == j):
        print("I=%r J=%r" % (i, j))
        print("I=%r J=%r" % (i, j+1))
        print("I=%r J=%r" % (i, j+2))
    elif int(i) == i:
        print("I=%r J=%r" % (i, j))
        print("I=%r J=%r" % (i, j+1))
        print("I=%r J=%r" % (i, j+2))
    elif int(j) == j:
        print("I=%r J=%r" % (i, j))
        print("I=%r J=%r" % (i, j+1))
        print("I=%r J=%r" % (i, j+2))
    else:
        print("I=%.1r J=%.1r" % (i, j))
        print("I=%.1r J=%.1r" % (i, j+1))
        print("I=%.1r J=%.1r" % (i, j+2))

    i += 0.2
    j += 0.2
#TODO: Consertar print