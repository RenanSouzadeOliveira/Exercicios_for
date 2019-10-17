f = "=" * 20
print(f)
print("10 TERMOS DE UMA PA".center(20))
print(f)

termo1 = int(input("Primeiro termo:"))
razao = int(input("Razão:"))
decimo = termo1 + (10 - 1) * razao

for x in range(termo1, decimo + razao, razao):
    print('{}'.format(x), end='-> ')
print("FIM")