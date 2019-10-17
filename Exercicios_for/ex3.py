s = 0
for x in range(1, 501):
    if (x % 2 != 0):
        if (x % 3 == 0):
            s += x
print("{}".format(s))