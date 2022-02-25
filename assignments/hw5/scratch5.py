def another_series():  # using mod %
    acc = 0
    total = 0
    terms = eval(input("Enter the number of terms: "))
    for i in range(terms):
        acc = acc % 6
        acc += 2
        print(acc, end=" ")
        total = total + acc
    print("\n", "sum = ", total)


another_series()