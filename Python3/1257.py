n = int(input())

A = ord("A")
for i in range(n):
    l = int(input())
    hash = 0
    for j in range(l):
        line = input()
        for idx, char in enumerate(line):
            hash += ord(char) - A + idx + j
    print(hash)