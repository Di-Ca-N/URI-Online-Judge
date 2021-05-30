try:
    while True:
        n, y = map(int, input().split())

        current_usernames = set()
        fora_do_padrao = 0

        for i in range(n):
            name = input()
            last_letter = " "
            username = []
            for letter in name:
                if letter != " " and last_letter == " ":
                    username.append(letter)
                last_letter = letter
            username = "".join(username)
            if username in current_usernames:
                fora_do_padrao += 1
            else:
                current_usernames.add(username)
        print(fora_do_padrao)
except EOFError:
    pass

