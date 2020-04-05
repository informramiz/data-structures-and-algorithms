"""
Author: Ramiz Raja
Created on: 24/02/2020
"""
def numberOfOffices(grid):
    count = 0
    is_office_going = False
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            value = grid[row][col]

            immediate_top = None
            if (row-1) >= 0:
                immediate_top = grid[row-1][col]

            immediate_before = None
            if (col-1) >= 0:
                immediate_before = grid[row][col-1]

            if value == 1:
                if not is_office_going and immediate_top != 1 and immediate_before != 1:
                    is_office_going = True

            elif value == 0:
                if is_office_going:
                    is_office_going = False
                    count += 1

            if is_office_going:
                is_office_going = False
                count += 1

    if is_office_going:
        count += 1

    return count


grid = [[1, 1, 0, 1, 1],
	    [1, 1, 1, 0, 0]]
count1 = numberOfOffices(grid)
print(count1)


grid = [[1, 1, 0, 0, 0],
	 [1, 1, 0, 0, 0],
	 [0, 0, 1, 0, 0],
	 [0, 0, 0, 1, 1]]
count1 = numberOfOffices(grid)
print(count1)

grid2 = [[1,1,1,1,1],
[1,0,0,0,1],
[1,0,0,0,0],
[1,1,1,0,1]]

count1 = numberOfOffices(grid2)
print(count1)