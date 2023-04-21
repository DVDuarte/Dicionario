qtdAvaliacoes = int(input("Digite a quantidade de avaliações: "))
qtdAlunos = int(input("Digite a quantidade de alunos: "))
alunos = {}

for i in range(qtdAlunos):
    nome = input("Digite o nome do aluno: ")
    notas = []
    for j in range(qtdAvaliacoes):
        nota = float(input(f"Digite a {j+1}ª nota do aluno: "))
        notas.append(nota)
    alunos[nome] = notas

mediaTotal = 0
for nome in alunos:
    soma = 0
    media = 0
    for j in alunos[nome]:
        soma = soma + j
    media = soma / qtdAvaliacoes
    print(f"A média do aluno {nome} é", media)
    mediaTotal = mediaTotal + media

mediaTotal = mediaTotal / qtdAlunos
print("A média da turma é ", mediaTotal)