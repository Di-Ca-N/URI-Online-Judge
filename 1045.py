lados = map(float, input().split())
c, b, a = sorted(lados)


if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    soma = b ** 2 + c ** 2
    if a**2 == soma:
        print("TRIANGULO RETANGULO")
    elif a**2 > soma:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif any((a == b, a == c, b == c)):
        print("TRIANGULO ISOSCELES")
