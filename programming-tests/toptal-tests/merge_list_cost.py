"""
Author: Ramiz Raja
Created on: 08/04/2020
"""


from queue import PriorityQueue

def function(A):
    if len(A) < 2:
        return 0
    elif len(A) == 2:
        return sum(A)

    min_queue = PriorityQueue()
    for n in A:
        min_queue.put_nowait(n)

    while min_queue.qsize() > 1:
        s1, s2 = min_queue.get_nowait(), min_queue.get_nowait()
        min_queue.put_nowait(s1 + s2)

    return min_queue.get_nowait()


output = function([100])
print(output)
output = function([100, 250])
print(output)
output = function([100, 250, 1000])
print(output)

output = function([100, 250, 25, 25])
print(output)