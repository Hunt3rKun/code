def theAge( age):
    age = int(age)
    if age == 1:
        return 10
    else:
        return theAge(age - 1) + 2
print(theAge(5))