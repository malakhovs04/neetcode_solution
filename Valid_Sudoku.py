<<<<<<< HEAD
def check(vals):
    data = dict()
    for i in vals:
        if i != '.':
            if i in data:
                return False
            data[i] = True
    return True



def isValidSudoku(board):
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        squares = [[] for _ in range(9)]
        for i in range(9):
             for j in range(9):
                  cols[i].append(board[i][j])
                  cols[i].append(board[i][j])
        for i in range(9):
             for j in range(9):
                if i < 3 and j < 3:
                        squares[0].append(board[i][j])
                elif i < 3 and j < 6:
                        squares[1].append(board[i][j])
                elif i < 3 and j < 9:
                       squares[2].append(board[i][j])
                elif i < 6 and j < 3:
                       squares[3].append(board[i][j])
                elif i < 6 and j < 6:
                       squares[4].append(board[i][j])
                elif i < 6 and j < 9:
                       squares[5].append(board[i][j])
                elif i < 9 and j < 3:
                       squares[6].append(board[i][j])
                elif i < 9 and j < 6:
                       squares[7].append(board[i][j])
                elif i < 9 and j < 9:
                       squares[8].append(board[i][j])

        for i in range(9):
              if not(check(rows[i])):
                    return False 
              if not(check(cols[i])):
                    return False 
              if not(check(squares[i])):
                    return False  
        return True  


                
        
            


board1 = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board1))

board2 = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

=======
def check(vals):
    data = dict()
    for i in vals:
        if i != '.':
            if i in data:
                return False
            data[i] = True
    return True


def isValidSudoku(board):
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        squares = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                cols[j].append(board[i][j])
                rows[i].append(board[i][j])
        for i in range(9):
            for j in range(9):
                if i < 3 and j < 3:
                    squares[0].append(board[i][j])
                elif i < 3 and j < 6:
                    squares[1].append(board[i][j])
                elif i < 3 and j < 9:
                    squares[2].append(board[i][j])
                elif i < 6 and j < 3:
                    squares[3].append(board[i][j])
                elif i < 6 and j < 6:
                    squares[4].append(board[i][j])
                elif i < 6 and j < 9:
                    squares[5].append(board[i][j])
                elif i < 9 and j < 3:
                    squares[6].append(board[i][j])
                elif i < 9 and j < 6:
                    squares[7].append(board[i][j])
                else:
                    squares[8].append(board[i][j])
        for i in range(9):
            if not(check(rows[i])):
                return False
            if not(check(cols[i])):
                return False
            if not(check(squares[i])):
                return False
        return True
                
        
            


board1 = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board1))

board2 = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

>>>>>>> 9dda5c45882b8ba8978b316d89ef05360b56d51d
print(isValidSudoku(board2))