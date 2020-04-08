"""
Author: Ramiz Raja
Created on: 07/04/2020
"""


def function(S, X, Y):
    points = {}
    max_y = max([abs(x) for x in X])
    max_x = max([abs(y) for y in Y])
    max_radius = max(max_x, max_y)
    for tag, x, y in zip(S, X, Y):
        x = abs(x)
        y = abs(y)
        if points.get(tag) is None and x <= max_radius and y <= max_radius:
            points[tag] = (x, y)
        elif abs(x) <= max_radius or abs(y) <= max_radius: # duplicate not allowed
            old_x, old_y = points[tag]
            new_x, new_y = None, None
            rejected_x, rejected_y = None, None
            if old_x <= max_radius and old_y <= max_radius:
                # keep the old point
                new_x, new_y = old_x, old_y
                rejected_x, rejected_y = x, y
            else:
                # use the new point as old point is out of range
                new_x, new_y = x, y
                rejected_x, rejected_y = x, y

            points[tag] = new_x, new_y
            if max_radius > rejected_x or max_radius > rejected_y:
                max_radius = min(rejected_x, rejected_y) - 1

    # now we have a valid radius, count points inside it
    count = 0
    for key in points:
        x, y = points[key]
        if abs(x) <= max_radius or abs(y) <= max_radius:
            count += 1

    return count


count = function('ABDCA', [2, -1, -4, -3, 3], [2, -2, 4, 1, -3])
print(count)
count = function('ABB', [1, -2, -2], [1, -2, 2])
print(count)