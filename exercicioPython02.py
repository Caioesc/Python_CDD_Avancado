#Altere o exercício anterior e mostre na tela ao final, ao final, o nome de cada aluno e sua respectiva posição no array

nomes = [" ", " ", " ", " ", " "]
tamanho = len(nomes)

for i in range(0, tamanho, 1):
    nomes[i] = input(f"Digite o nome do {i+1}º aluno: ")

for i in range(0, tamanho, 1):
    print (f"{nomes[i]} está na posição {i} do array.")