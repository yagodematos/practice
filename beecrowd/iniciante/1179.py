par = []
impar = []
for _ in range(15):
    x = int(input())

    if x % 2 == 0:
        if len(par) < 5:
            par.append(x)
        else:
            for i, v in enumerate(par):
                print(f"par[{i}] = {v}")
            par = []
            par.append(x)
    else:
        if len(impar) < 5:
            impar.append(x)
        else:
            for i, v in enumerate(impar):
                print(f"impar[{i}] = {v}")

            impar = []
            impar.append(x)

if impar:
    for i, v in enumerate(impar):
        print(f"impar[{i}] = {v}")
if par:
    for i, v in enumerate(par):
        print(f"par[{i}] = {v}")
