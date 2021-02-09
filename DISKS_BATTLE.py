board = [
    ['y','y','r','y','y','r','y'],
    ['y','y','y','r','y','r','r'],
    ['r','r','y','y','r','y','r'],
    ['y','y','r','r','r','r','y'],
    ['r','y','y','y','r','r','r'],
    ['r','y','y','y','r','r','r']
]
BOARD_ROWS = 6
BOARD_COLUMNS = 7
def isInBoard(comb):
    global BOARD_ROWS, BOARD_COLUMNS
    for n in comb:
        print(n)
        if (n[0] < 0 or n[1] < 0) or (n[0] >= BOARD_ROWS or n[1] >= BOARD_COLUMNS):
            return False
    return True

test = isInBoard([[0, 1], [0, 2], [0, 6], [0, 7]])
print(test)
# array is a combination of 4 cells ([[r,c],[r+1,c],[r+2,c],[r+3,c]]) for example
# returns True if all the cells of the combination are in the board
# returns False if not

def getCombinationsFrom(row, col):
    combinations = [
        # vertical combinations
        [[row, col], [row + 1, col], [row + 2, col], [row + 3, col]],
        [[row - 1, col], [row, col], [row + 1, col], [row + 2, col]],
        [[row - 2, col], [row - 1, col], [row, col], [row + 1, col]],
        [[row - 3, col], [row - 2, col], [row - 1, col], [row, col]],
        # horizontal combinations
        [[row, col], [row, col + 1], [row, col + 2], [row, col + 3]],
        [[row, col - 1], [row, col], [row, col + 1], [row, col + 2]],
        [[row, col - 2], [row, col - 1], [row, col], [row, col + 1]],
        [[row, col - 3], [row, col - 2], [row, col - 1], [row, col]],

        # diagonal-asc combinations
        [[row, col], [row + 1, col + 1], [row + 2, col + 2], [row + 3, col + 3]],
        [[row - 1, col - 1], [row, col], [row + 1, col + 1], [row + 2, col + 2]],
        [[row - 2, col - 2], [row - 1, col - 1], [row, col], [row + 1, col + 1]],
        [[row - 3, col - 3], [row - 2, col - 2], [row - 1, col - 1], [row, col]],
        # diagonal-desc combinations
        [[row, col], [row + 1, col - 1], [row + 2, col - 2], [row + 3, col - 3]],
        [[row - 1, col + 1], [row, col], [row + 1, col - 1], [row + 2, col - 2]],
        [[row - 2, col + 2], [row - 1, col + 1], [row, col], [row + 1, col - 1]],
        [[row - 3, col + 3], [row - 2, col + 2], [row - 1, col + 1], [row, col]]
    ]
    return combinations


def hasSameSign(sign, comb):
    global board
    counter = 0
    isSameSign = False
    for n in comb:
        row = n[0]
        col = n[1]
        if sign == board[row][col]:
            counter += 1
    if counter == 4:
        isSameSign = True
    return isSameSign
#returns wether or not a combination of 4 cells has the same sign or not
