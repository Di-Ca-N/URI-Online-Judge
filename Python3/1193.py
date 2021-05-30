n = int(input())

for i in range(n):
    number, base = input().split()
    
    print(f"Case {i + 1}:")
    if base == 'bin':
        in_dec = int(number, 2)
        in_hex = hex(in_dec)[2:]

        print(f"{in_dec} dec")
        print(f"{in_hex} hex")
    elif base == 'hex':
        in_dec = int(number, 16)
        in_bin = bin(in_dec)[2:]

        print(f"{in_dec} dec")
        print(f"{in_bin} bin")
    else:
        dec = int(number)
        in_bin = bin(dec)[2:]
        in_hex = hex(dec)[2:]

        print(f"{in_hex} hex")
        print(f"{in_bin} bin")
    print()
