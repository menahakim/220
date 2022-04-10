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


def is_prime(number):
    i = 2
    while i < number:
        divided_by = number % i
        if divided_by == 0:
            return False
        i += 1
    return True


def goldbach(number):
    odd = number % 2 == 1
    if odd:
        return None
    else:
        prime1 = 1
        prime2 = 1
        while (prime1 + prime2) < number:
            prime2 = 1
            while (prime1 + prime2) < number:
                total = prime1 + prime2
                if total == number:
                    return [prime1, prime2]
                else:
                    prime = False
                    while not prime:
                        prime2 += 1
                        prime = is_prime(prime2)

            total = prime1 + prime2
            if total == number:
                return [prime1, prime2]
            else:
                prime = False
                while not prime:
                    prime1 += 1
                    prime = is_prime(prime1)
        return [-1, -1]


if __name__ == '__main__':
        fibonacci(3)
        print(goldbach(20))
        print(goldbach(2))
        print(goldbach(4))
        print(goldbach(36))
        print(goldbach(1024))
