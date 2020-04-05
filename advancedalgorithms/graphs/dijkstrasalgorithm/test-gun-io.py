"""
Author: Ramiz Raja
Created on: 29/02/2020
"""

def fibonnoci_sum():
    rangeEnd = 10_000
    prev_prev_fibonnoci = 0
    prev_fibonnoci = 1

    total_sum = 1
    next_fibonnoci = 1
    while next_fibonnoci < rangeEnd:
        if next_fibonnoci % 2 != 0:
            total_sum += next_fibonnoci

        prev_prev_fibonnoci = prev_fibonnoci
        prev_fibonnoci = next_fibonnoci
        next_fibonnoci = prev_prev_fibonnoci + prev_fibonnoci


    return total_sum


result = fibonnoci_sum()
print(result)

# def is_palindrome(numberStr):
#     numberStr = numberStr.lower()
#     return numberStr == numberStr[::-1]
#
# def palindrome_sum():
#     p_sum = 0
#     for n in range(10_000):
#         if is_palindrome(str(n)):
#             p_sum += n
#
#     return p_sum
#
#
#
# result = palindrome_sum()
# print(result)