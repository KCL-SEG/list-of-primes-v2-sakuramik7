"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 0
    if number_of_primes <= 0:
        raise ValueError
    if number_of_primes > 0:
        p1 = 2
        list.append(p1)
        count = count + 1
    if number_of_primes > 1:
        index = p1 + 1
        mul = 1
        flag = False
        while count < number_of_primes:
            for x in range(2, index):
                if index % x == 0:
                    flag = True
            if flag == False:
                list.append(index)
                count = count + 1
            flag = False
            index = index + 1
    return list
