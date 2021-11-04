a = int(input())
s = int(input())

visible = 0

for i in range(s):
    f = int(input())
    if f * a >= 40000000:
        visible += 1

print(visible)