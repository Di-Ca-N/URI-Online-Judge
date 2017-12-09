a = int(input())

for i in range(a):
    out = ""
    num = int(input())
    if num % 2 == 0:
        out += "EVEN "
    else:
        out += "ODD "

    if num < 0:
        out += "NEGATIVE"
    elif num > 0:
        out += "POSITIVE"
    else:
        out = "NULL"

    print(out)
