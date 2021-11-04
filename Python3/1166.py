n = int(input())

for i in range(n):
    t = int(input())
    hastes = [0] * t
    can_place = True
    current = 1
    current_idx = 0
    while can_place:
        if ((hastes[current_idx] + current) ** 0.5).is_integer() or hastes[current_idx] == 0:
            hastes[current_idx] = current
            current += 1
            current_idx = 0
        else:
            current_idx += 1
            if current_idx == t:
                can_place = False

    print(current - 1)
