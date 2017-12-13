valores = input()

while valores != "0":
    a, b, c = map(int,valores.split())
    area = a * b
    area_terreno = area * (100 / c)
    lado = int(area_terreno**0.5)
    print(lado)
    valores = input()
