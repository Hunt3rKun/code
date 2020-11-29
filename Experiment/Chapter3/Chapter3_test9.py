number =13*10E7
counter = 0
while number <= 20*10E7:
    number = number*(1+0.008)
    counter += 1
print(counter)