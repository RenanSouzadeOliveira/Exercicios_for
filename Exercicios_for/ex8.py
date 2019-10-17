frase = input("Digite uma frase:").strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

print("Você digitou:{}".format(junto), end="")
print(", a frase invertida é:", end=" ")
for letra in range(len(junto) - 1, -1, -1):
    inverso += ''.join(junto[letra])
print(inverso)

if (junto == inverso):
    print("É um palíndromo")
else:
    print("Não é um palíndromo")




