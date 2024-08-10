A = list()

for _ in range(100):
    A.append(float(input()))

for i, x in enumerate(A):
    if x <= 10:
        print(f"A[{i}] = {x:.1f}")
