num = int(input("Entre com o número que você deseja calcular a taboada:"))
r = 0
for x in range(0, 11):
    r = num * x
    print("{0} x {1} = {2}".format(num, x, r))