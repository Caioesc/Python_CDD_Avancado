vetor = [0] * 5
tamanho = len(vetor)

for i in range(0, tamanho, 1):
    vetor[i] = int(input(f"Digite o {i+1}º valor: "))

for i in range(tamanho-1, -1, -1):
    print(vetor[i], end=" ")