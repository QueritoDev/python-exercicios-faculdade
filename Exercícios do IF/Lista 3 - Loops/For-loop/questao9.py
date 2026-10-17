notasAluno = 0.0
media = 0.0
for i in range (1,6):
    notasAluno = float(input(f"Digite a nota {i} do aluno: "))
    media += notasAluno

media = media / 5

print(f"A media do aluno foi: {media}")