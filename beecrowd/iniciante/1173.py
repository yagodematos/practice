x = int(input())

N = []

for i in range(10):
    N.append(x)
    x *= 2


for i in range(10):
    print(f"N[{i}] = {N[i]}")
