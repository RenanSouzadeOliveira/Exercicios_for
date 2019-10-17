peso_maior = 0
peso_menor = 0
for pes in range(1, 6):
    peso = float(input("Digite o peso da {}ª pessoa:".format(pes)))

    if pes == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso
print("O maior peso digitado foi: {}".format(peso_maior))
print("O menor peso digitado foi: {}".format(peso_menor))




