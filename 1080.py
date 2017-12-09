todos = []

for i in range(100):
    todos.append(int(input()))

maior = max(todos)

print(maior)
print(todos.index(maior)+1)
