texto = input("Digite o texto desejado: ")
vogais = "aeiou"
soma = 0

for i in range(len(texto)):
    for x in range(len(vogais)):
        if vogais[x] == texto[i]:
            soma += 1
print(f"O número de vogais no texto é de: {soma}")



