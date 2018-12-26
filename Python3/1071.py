a = int(input())
b = int(input())
total = 0
if b < a:
    a, b = b, a

for i in range(a+1, b):
    if i % 2 == 1:
        total += i

print(total)