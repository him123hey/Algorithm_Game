arr = [
    ['y','y','r','y','y','r','y'],
    ['y','y','y','r','y','r','r'],
    ['r','r','y','y','r','y','r'],
    ['y','y','r','r','r','r','y'],
    ['r','y','y','y','r','r','r'],
    ['r','y','y','y','r','r','r']
]
# check sign on Row
def signOnRow(grid, row, sign):
    counter = 0
    for n in grid[row]:
        if sign == n:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True
    return False
# check sign on column
def signOnCol(grid, col, sign):
    counter = 0
    for i in range(len(grid)):
        if sign == grid[i][col]:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True
    return False    
# check diagonal sign
def signOnDiagonal(grid, col, sign):
    counter1 = 0
    counter2 = 0
    if row == 0:
        for i in range(len(grid)):
            print(grid[col][row + i])

print(signOnDiagonal(arr, 0, 2, 'r'))
# check have won
def isWon(grid, sign):
    if signOnDiagonal(grid, sign):
        return True
    for i in range(len(grid)):
        if signOnCol(grid, i, sign) or signOnRow(grid, i, sign):
            return True
    return False

# if isWon(arr2, "y"):
#     print("Y WON")

# # elif hasSignWon(arr, "r"):
# #     print("R WON")

# else:
#     print("NO WINNER")