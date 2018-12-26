a = int(input())

while a != 0:
    if a % 2 == 1:
        a += 1
    print(sum(range(a, a+10, 2)))
    a = int(input())
