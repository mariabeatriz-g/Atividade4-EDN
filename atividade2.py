# Lista para armazenar as notas
notas = []

# Solicita a quantidade de alunos
quantidade = int(input("Quantos alunos você deseja registrar? "))

# Loop para registrar as notas
for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

# Calcula a média
media = sum(notas) / len(notas)

# Exibe a média da turma
print("\nNotas registradas:", notas)
print("Média da turma: {:.2f}".format(media))