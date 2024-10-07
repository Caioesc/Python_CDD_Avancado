"""Escreva um algortimos que solicite ao usuário a entrada de 5 nomes, e que exiba a lista desses nomes na tela.
Após exibir essa lista, o programa deve mostrar também os nomes na ordem inversa em que o usuário os digitou, um por linha."""

nomes = [" "] * 5
tamanho = len(nomes)

for i in range(tamanho):
    nomes[i] = input(f"Digite o {i+1}º nome: ")
print(f"A lista de nomes é: {nomes}")

#nomes.reverse()
#print(nomes)

for j in range(tamanho -1 , -1, -1):
    print(nomes[j])