media = 0
mulheres_menor = 0
for pes in range(1, 5):
    print("---- {}ª PESSOA ----".format(pes))
    nome = input("Nome:")
    idade = int(input("Idade:"))
    sexo = input("M/F:").upper()
    media += idade

    if (sexo == 'M'):
        if (pes == 1):
            idade_maior = idade
        else:
            if (idade > idade_maior):
                idade_maior = idade
                nome_mais_velho = nome
    if (sexo == 'F'):
        if (idade < 18):
            mulheres_menor += 1
media = media / 4
print("A média de idade do grupo é: {}.".format(media))
print("O homem mais velho tem {} anos e se chama {}.".format(idade_maior,nome_mais_velho))
print("Ao todo são {} mulheres menor de idade.".format(mulheres_menor))
