nomes = [" ", " ", " ", " ", " "]
tamanho = len(nomes)

for i in range(0, tamanho, 1):
    nomes[i] = input(f"Digite o nome do {i+1}º aluno: ")

for j in range(0, tamanho, 1):
    print (nomes[j], end=" ")