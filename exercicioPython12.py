"""Faça um algoritmo que leia 10 valores do tipo inteiro e armazene-os em um vetor. A seguir, o algortimo deverá informar:
1- Todos os números pares que existem no vetor;
2- o maior e o menor valor existente no vetor;
3 - quantos dos valores são maiores que a média desses valores."""

valores = [0] * 10
tamanho = len(valores)
pares = []
maiores = []
soma = 0

for i in range(tamanho):
    valores[i] = int(input(f"Digite o {i+1}º valor: "))
    if valores[i] % 2 == 0:
        pares.append(valores[i])
print(f"\nNúmeros pares digitados: {pares}")

maior = valores[0] #maior = max(valores)
menor = valores[0] #menor = min(valores)
for k in range (1, tamanho):
    if valores[k] > maior:
        maior = valores[k]
    if valores[k] < menor:
        menor = valores[k]

print(f"Maior número: {maior} \nMenor número: {menor}")

for m in range(tamanho):
    soma += valores[m]
media = soma/tamanho

for n in range(tamanho):
    if valores[n] > media:
        maiores.append(valores[n])

print(f"A lista possui {len(maiores)} números maiores do que a média({media}): {maiores}")











