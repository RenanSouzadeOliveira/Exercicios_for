s = 0
for x in range (0, 6):
    num = int(input("Entre com um número inteiro:"))
    if (num % 2 == 0):
        s += num
print("A soma dos pares é {}".format(s))