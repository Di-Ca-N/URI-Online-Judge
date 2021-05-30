n = int(input())

for i in range(n):
    m = int(input())
    alunos = [int(x) for x in input().split()]
    alunos_em_ordem = sorted(alunos, reverse=True)
    no_lugar = 0

    for aluno, aluno_ordenado in zip(alunos, alunos_em_ordem):
        if aluno == aluno_ordenado:
            no_lugar += 1
    print(no_lugar)

