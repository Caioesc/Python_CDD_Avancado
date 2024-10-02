"""Escreva um código que permita a leitura das notas de uma turma de 5 alunos e guarde num vetor, calcular a média
da turma e contar quantos alunos obtiveram nota acima desta média calculada. Escrever a média da turma e
o resultado da contagem."""

notas = [0.0] * 5
tamanho = len(notas)
soma = 0
maiorMedia = 0

for i in range(0, tamanho, 1):
    notas[i] = float(input(f"Digite a nota do {i+1}º aluno: "))

for x in range(0, tamanho, 1):
    soma = soma + notas[x]

media = soma/tamanho

for y in range(0, tamanho, 1):
    if notas[y] > media:
        maiorMedia += 1

print(f"\nA média da turma é {media} e a quantidade de notas acima da média da turma é de {maiorMedia}")

