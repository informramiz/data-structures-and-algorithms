"""
Problem Statement
Find and return the nth row of Pascal's triangle in the form a list. n is 0-based.

For example, if n = 4, then output = [1, 4, 6, 4, 1].

To know more about Pascal's triangle: https://www.mathsisfun.com/pascals-triangle.html
"""


def nth_row_pascal(n):
    # first row (row #0) is always [1]
    current_row = [1]
    # first row (row #0) is already known so start with row #1 and go till row #n (n inclusive here as
    # we want the nth term)
    for r in range(1, n+1):  # [1, n]
        previous_row = current_row
        # each Pascal triangle row starts with 1
        current_row = [1]
        # Each row #r has total columns=r+1 or in other words column indexes=[0, r],
        # first and last column of each row is 1 so range is [1, r-1] because first column ([1]) is already added
        # and we will add the last column ([1]) after this loop
        for c in range(1, r):  # [1, r-1]
            next_number = previous_row[c] + previous_row[c-1]
            current_row.append(next_number)

        # add the last column which is always 1
        current_row.append(1)

    return current_row


def test_pascal():
    output = nth_row_pascal(0)
    assert output == [1], f"output: {output}"

    output = nth_row_pascal(1)
    assert output == [1, 1], f"output: {output}"

    output = nth_row_pascal(2)
    assert output == [1, 2, 1], f"output: {output}"

    output = nth_row_pascal(3)
    assert output == [1, 3, 3, 1], f"output: {output}"

    output = nth_row_pascal(4)
    assert output == [1, 4, 6, 4, 1], f"output: {output}"


test_pascal()
