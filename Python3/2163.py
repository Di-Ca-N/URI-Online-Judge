l, c = [int(x) for x in input().split()]
matriz = [[0 for _ in range(c)] for _ in range(l)]

possible_sabers = []

for i in range(l):
    for j, v in enumerate(input().split()):
        v = int(v)
        matriz[i][j] = v
        if v == 42:
            possible_sabers.append((i, j))

final = (0, 0)

pattern = [
    (-1 , -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1),
]

for a, b in possible_sabers:
    for x, y in pattern:
        adx = a + x
        ady = b + y
        
        if 0 <= adx < l and 0 <= ady < c:
            if matriz[adx][ady] != 7:
                break
        else:
            break
    else:
        final = a + 1, b + 1
    
print(*final)

