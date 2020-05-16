import numpy as np
from datetime import datetime


grid= []

print("Enter rows as just consecutive numbers without any spaces.")
print("An empty cell is equivalent to a zero(0).")
for i in range(9):
    grid.append([])
    print("Enter row:", i + 1)
    row = input()
    nums = [int for int in row]
    for j in range(9):
        grid[i].append(int(nums[j]))

print("Your board is:\n", np.matrix(grid))


def test(y, x, n):
    global grid
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

t0 = datetime.now()

def solveSudoku():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x]  == 0:
                for n in range(1,10):
                    if test(y,x,n):
                        grid[y][x] = n
                        solveSudoku()
                        grid[y][x] = 0
                return
    print("\nYour solution is:\n", np.matrix(grid))
    t1 = datetime.now()
    global t0
    totaltime = t1 - t0
    print('Time elapsed (hh:mm:ss.ms) {}'.format(totaltime))
    input("\nHit enter for more solutions, if any")

solveSudoku()