a = int(input())
dentro, fora = 0, 0

for i in range(a):
    if 10 <= int(input()) <= 20:
        dentro += 1
    else:
        fora += 1

print("{} in".format(dentro))
print("{} out".format(fora))
