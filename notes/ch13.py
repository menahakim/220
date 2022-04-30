def linear_search(search_list, target):
    for i in range(len(search_list)):
        if search_list[i] == target:
            return i
        return -1


def binary_search(search_list, target):
    left_index = 0
    right_index = len(search_list) - 1
    while left_index <= right_index:
        middle_index = (right_index + left_index) // 2
        middle_value = search_list(middle_index)
        if middle_value == target:
            return middle_index
        elif middle_value < target:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1
    return -1


def print_repeat(s, n):
    if n == 0:
        return
    else:
        print(s)
        print_repeat(s, n - 1)


def sum_list(my_list):
    if len(my_list) == 0:
        return 0
    else:
        my_list[0] + sum(my_list[1:])


def sum_list_tail(my_list, acc):
    if len(my_list) == 0:
        return acc
    else:
        acc = my_list[0] + acc
        return sum_list_tail(my_list[:1], acc)


def fib_recursive(n):
    if n < 3:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)


def fib(n):  # better function calculates quicker
    curr = 1
    prev = 1
    for i in range(n-2):
        sum = curr + prev
        prev = curr
        curr = sum
    return curr


if __name__ == '__main__':
    # print(fib_recursive(37))
    print(fib(100))
    # print_repeat("hi", 3)
    # print(sum_list([3, 7, 5]))
    # print(sum_list([3, 7, 5], 0))
    # my_list = [3, 4, 2, 1, 9, 10, 81, 45]
    # target = 7
    # # res = linear_search(my_list, target)
    # my_list.sort()
    # res = binary_search(my_list, target)
    # if res >= 0:
    #     print('found it!', res)
    # else:
    #     print('nope!', res)

# IMPORTANT WILL BE ON EXAM!!!
# a notation to test the efficiency of an algorithm is called big O
# stands for order of approximation
# linear search best case scenario is if the whatever you are looking for is first in the last
# worst case is if it is the last item in the list aka length of list
# binary search best case scenario is if item is right in the middle of list
# worst case scenario would be the ends of the list
# binary examples
# 8 items 4 searches
# 16 items 5 searches
# 32 items 6 searches
# O(log2n + 1)
# 1 is not there if looking at millions of comparisons because it is insignificant
# ON THE EXAM KNOW BEST AND WORST CASE SCENARIO FOR LINEAR AND BINARY SEARCH
# Best Case for Linear is 0(1) first item in the list
# Worst case for Linear is 0(n) go through all items in the list
# Best case for Binary 0(1)
# Worst case for linear 0(log n)
# when you call a function inside of itself that is called a recursion
# Recursive function needs to have a base case to exit the recursion
# Stack Overflow is when a computer runs out of memory

