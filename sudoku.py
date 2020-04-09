def FindUnused(mat, pts):
    for i in range(9):
        for j in range(9):
            if mat[i][j] == 0:#found a zero so assign coordinates
                pts[0] = i
                pts[1] = j

                return True
    return False

def UsedInCol(mat, col, num):
    for i in range(9):
        if mat[i][col] == num:
            return True

    return False

def UsedInRow(mat, row, num):
    for i in range(9):
        if mat[row][i] == num:
            return True

    return False

def UsedInBox(mat, x, y, num):
    for i in range(3):
        for j in range(3):
            if mat[i+x][j+y] == num:
                return True

    return False

def CanUse(mat, x, y,  num):
    return not UsedInRow(mat, x, num) and not UsedInCol(mat, y, num) and not UsedInBox(mat, x-(x%3), y-(y%3), num)

def Solve(board):
    points = [0,0]

    if not FindUnused(board, points):
        return True

    for i in range(1,10):#check compatibility for 1-9 in matrix
        if CanUse(board, points[0], points[1], i):
            board[points[0]][points[1]] = i

            if Solve(board):#solved
                return True

            board[points[0]][points[1]] = 0#reset spot

    return False

board = [[6, 0, 0, 3, 0, 5, 8, 7, 0],
         [0, 8, 0, 0, 2, 0, 0, 0, 0],
         [0, 0, 7, 8, 9, 0, 0, 5, 6],
         [0, 6, 0, 0, 7, 0, 1, 0, 0],
         [4, 0, 3, 1, 6, 2, 0, 0, 8],
         [9, 0, 1, 0, 3, 0, 7, 6, 4],
         [0, 0, 0, 0, 0, 3, 0, 0, 7],
         [2, 3, 0, 6, 0, 0, 9, 0, 0],
         [7, 1, 0, 0, 5, 4, 0, 0, 3]]

print("start")
if Solve(board):
    for i in range(9):
        print(board[i])
print("end")

# solution for reference
# [6,9,2, 3,4,5, 8,7,1],
# [1,8,5, 7,2,6, 3,4,9],
# [3,4,7, 8,9,1, 2,5,6],
# [5,6,8, 4,7,9, 1,3,2],
# [4,7,3, 1,6,2, 5,9,8],
# [9,2,1, 5,3,8, 7,6,4],
# [8,5,6, 9,1,3, 4,2,7],
# [2,3,4, 6,8,7, 9,1,5],
# [7,1,9, 2,5,4, 6,8,3]
