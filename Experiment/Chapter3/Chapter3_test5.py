counter = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and i != k and j != k:
                counter += 1
                print("{}{}{}".format(i, j, k), end=" ")
print("共{}种组合".format(counter))