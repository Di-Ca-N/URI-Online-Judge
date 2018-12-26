a, b = map(int, input().split())

while a != 0 and b != 0:
    if a > 0 and b > 0:
        print("primeiro")
    elif a < 0 < b:
        print("segundo")
    elif a < 0 and b < 0:
        print("terceiro")
    elif a > 0 > b:
        print("quarto")
    a, b = map(int, input().split())
