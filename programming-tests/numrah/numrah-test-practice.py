"""
Author: Ramiz Raja
Created on: 05/04/2020

Find Intersection
Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements:
the first element will represent a list of comma-separated numbers sorted in ascending order, the second element
will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string
containing the numbers that occur in elements of strArr in sorted order. If there is no intersection,
return the string false.

Examples
Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Output: 1,4,13
Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
Output: 1,9,10
"""

def find_intersection(string):
    str1 = string[0]
    str2 = string[1]
    set1 = set(str1.split(","))
    set2 = set(str2.split(","))
    intersection = set2.intersection(set1)
    int_list = [int(i) for i in intersection]
    return sorted(int_list)


input1 = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
output = find_intersection(input1)
assert (output == [1, 4, 13])
