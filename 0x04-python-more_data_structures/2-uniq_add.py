#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = []
    for num in my_list:
        if num not in unique_integers:
            unique_integers.append(num)

    total = 0
    for num in unique_integers:
        total += num
    return (total)
