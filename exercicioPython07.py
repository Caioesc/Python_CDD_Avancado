"""Faça um código para ler um vetor de 10 números. Após isto, ler mais um número
qualquer, calcular e escrever quantas vezes esse número aparece no vetor"""

numeros = [0]*10
tamanho = len(numeros)
cont = 0

for i in range(tamanho):
    numeros[i] = int(input(f"Digite o {i+1}º número do vetor: "))

num = int(input("Digite um número qualquer: "))

for x in range(tamanho):
    if num == numeros[x]:
        cont += 1

print(f"O número {num} apareceu {cont} vezes no array {numeros}")