num = int(input("Digite um número:"))
c = 0
for x in range (1, num+1):
    r = num % x
    if (r == 0):
        print('\33[1;33m', end=" ")
        c += 1
    else:
        print('\33[1;31m', end=" ")
    print("{}".format(x), end=" ")
if (c == 2):
    print("\nnúmero primo")
else:
    print("\nnúmero não é primo")