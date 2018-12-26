
def fat(num):
    if num > 1:
        return fat(num-1)*num
    else:
        return 1


a = int(input())

print(fat(a))
