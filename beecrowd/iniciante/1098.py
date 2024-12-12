# for i in [x / 10.0 for x in range(0, 21, 2)]:
    # for j in range(3):
        # if i == 0.0 or i == 1.0 or i == 2.0:
            # i = int(i)

        # print(f"I={i} J={j+1+i}")

for i in [x / 10.0 for x in range(0, 21, 2)]:
    for j in range(1, 4):
        if i.is_integer():
            print(f"I={int(i)} J={int(j+i)}")
        else:
            print(f"I={i} J={j+i}")
