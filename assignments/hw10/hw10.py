def fibonacci(n):
    count = 2
    value1 = 0
    value2 = 1
    result = 0
    if n == 1 or n == 2:
        return 1
    if n < 1:
        return None

    while count <= n:
        result = value1 + value2
        value1 = value2
        value2 = result
        count += 1
    return result


def double_investment(principle, rate):
    year = 0
    double = 2 * principle
    while principle < double:
        a = principle * (1 + rate)
        year += 1
        principle = a
    return year


def syracuse(x):
    my_list = [x]
    while x != 1:
        if x % 2 == 1:
            j = (x * 3) + 1
            my_list.append(j)
            x = j
        elif x % 2 == 0:
            j = x / 2
            my_list.append(j)
            x = j
    return my_list


def goldbach(number):
    pass


if __name__ == '__main__':
        fibonacci(3)
