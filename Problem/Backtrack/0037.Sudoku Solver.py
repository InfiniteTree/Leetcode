class Solution:
    def isValid(self, row, col, num, board):
        # Check in a col
        for i in range(len(board)):
            if board[i][col] == str(num):
                return False
        
        # Check in a row
        for j in range(len(board[0])):
            if board[row][j] == str(num):
                return False
        
        # Check in a sub-box
        row_i = row // 3
        col_i = col // 3
        #if k not in board[row_i*3:(row_i+1)*3][[col_i*3:(col_i+1)*3]]
        for i in range(row_i*3, (row_i+1)*3):
            for j in range(col_i*3, (col_i+1)*3):
                if board[i][j] == str(num):
                    return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n_row, n_col = len(board), len(board[0])
        ret = False
        def backtracking(board):
            for i in range(n_row):
                for j in range(n_col):
                    if board[i][j] == ".":
                        for k in range(1, 10):
                            if self.isValid(i, j, k, board):
                                board[i][j] = str(k)
                                ret = backtracking(board)
                                if ret:
                                    return True
                                board[i][j] = "."
                        return False
            return True
        
        backtracking(board)
        return board  
