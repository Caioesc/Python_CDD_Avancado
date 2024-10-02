"""Preencher um vetor A com 10 números. Logo em seguida, ler mais um número e guardar em uma variável x.
Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor x. No final imprimir o vetor M."""

A = [0] * 10
M = [0] * 10
tamanho = len(A)

for i in range(0, tamanho, 1):
    A[i] = int(input(f"Digite o {i+1}º valor: "))

x = int(input("\nDigite o valor de X: "))

for j in range(0, tamanho, 1):
    M[j] = A[j]*x

print(M)


