def count_invs(n, array):
    visited = set()
    i = 0
    total = 0
    while i != n:
        if i not in visited:
            cycle = 0
            next_i = array[i]
            while next_i not in visited:
                visited.add(next_i)
                next_i = array[next_i]
                cycle += 1
            total += (cycle - 1) % 2
        i += 1
    return total

n, *nums = [int(x) - 1 for x in input().split()]
while n + 1 != 0:
    invs = count_invs(n + 1, nums)
    if invs % 2 == 1:
        print("Marcelo")
    else:
        print("Carlos")
    
    n, *nums = [int(x) - 1 for x in input().split()]
