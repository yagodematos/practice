for i in [x / 10.0 for x in range(0, 21, 2)]:
    for j in range(3):
        if i == 0.0 or i == 1.0 or i == 2.0:
            i = int(i)

        print(f"I={i} J={j+1+i}")
