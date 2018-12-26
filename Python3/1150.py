a = int(input())
b = int(input())

while b <= a:
    b = int(input())

cont = 1

while sum(range(a,a+cont)) < b:
    cont += 1

print(cont)
