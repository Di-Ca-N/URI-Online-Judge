def merge_sort_and_count(array, left, right):
    if left >= right:
        return 0

    m = (left + right) // 2

    inv1 = merge_sort_and_count(array, left, m)
    inv2 = merge_sort_and_count(array, m + 1, right)

    inversoes = inv1 + inv2

    s1 = left
    s2 = m + 1

    while s1 <= m and s2 <= right:
        if array[s1] <= array[s2]:
            s1 += 1
            continue
        
        inversoes += s2 - s1
        v = array[s2]
        for i in range(s2, s1 - 1, -1):
            array[i] = array[i - 1]

        array[s1] = v

        s2 += 1
        s1 += 1
        m += 1

    return inversoes
   

qtd, *seq = [int(x) for x in input().split()]

while qtd != 0:
    inversions = merge_sort_and_count(seq, 0, qtd - 1)
    print(inversions)
    if inversions % 2 == 1:
        print("Marcelo")
    else:
        print("Carlos")

    qtd, *seq = [int(x) for x in input().split()]
