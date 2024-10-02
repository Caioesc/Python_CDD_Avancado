texto = input("Digite o texto desejado: ")
vogais = "aeiou"
soma = 0

for i in texto:
    if i in vogais:
        soma += 1
print(f"O número de vogais no texto é de: {soma}")




