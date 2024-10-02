"""Altere o sistema anterior (exercicioPython06) e faça um sistema de login, pedindo a senha do
usuário e mostrando seu nome e a mensagem, login efetuado com sucesso."""

nomes = [" "] * 5
senhas = [0] * 5
tamanho = len(nomes)
opcao = 0
tentativas = 0

while opcao != 4:
    opcao = int(input(f"\nDigite a opção desejada: \n1 - Cadastro \n2 - Login \n3 - Mostrar usuários \n4 - Sair "))
    if opcao == 1:
        for i in range(tamanho):
            nomes[i] = input(f"Digite seu nome, usuário {i+1}: ")
            senhas[i] = int(input(f"Digite a senha, usuario {i+1}:"))

    elif opcao == 2:
        usuario = input("Digite seu nome de usuário: ")
        for i in range(tamanho):
            if usuario == nomes[i]:
                while tentativas < 3:
                    senha = int(input("Digite sua senha: "))
                    if senha == senhas[i]:
                        print("Login efetuado com sucesso!")
                        opcao = 4
                        break
                    else:
                        print("Senha incorreta, tente novamente!")
                        tentativas += 1
                        if tentativas == 3:
                            print("Tentativas de senha excedidas! Login bloqueado.")
                            opcao = 4
        if usuario not in nomes:
            print("Usuário não está no cadastro!\n")

    elif opcao == 3:
        print(f"A lista de cadastrados é: {nomes}")

    elif opcao == 4:
        print("Programa encerrado.")






