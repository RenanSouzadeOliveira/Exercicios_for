from datetime import date
atual = date.today().year
cont_maior = 0
cont_menor = 0
idade = " "
for x in range(1, 8):
    print("Digite em que ano a {}ª pessoa nasceu:".format(x), end=" ")
    idade = int(input())

    if ((atual - idade) < 18):
        cont_menor += 1
    else:
        cont_maior +=1
print("No total tivemos {} pessoas de menor, e {} de maior.".format(cont_menor,cont_maior))