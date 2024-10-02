"""Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada lista em um array
diferente, após completar a digitação, imprimir, nome, senha e posição dos dados no array."""

nomes = [" "] * 5
senhas = [0] * 5
tamanho = len(nomes)

for i in range(tamanho):
    nomes[i] = input(f"Digite seu nome, usuário {i+1}: ")
    senhas[i] = int(input(f"Digite a senha, usuario {i+1}:"))

for x in range(tamanho):
    print(f"Usuário {x+1}: \nNome: {nomes[x]} \nSenha: {senhas[x]} \nPosição no array: {x}\n")
