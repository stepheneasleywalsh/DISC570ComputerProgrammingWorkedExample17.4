x = int(input('Give me a number more 1 or more, 100 or less but even: '))

if x >= 1:
    if x <= 100:
        if x%2 == 0:
            print("Thank you")
        else:
            print("This is not even, it's odd")
    else:
        print("x is too big")
else:
    print("x is too small")
