class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def isValid(self, chessboard, row, col, n):
        # Check the column
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False
        # Check the upperleft
        i, j = row-1, col - 1
        while i>=0 and j>=0:
            if chessboard[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        # Check the upperright
        i, j = row-1, col + 1
        while i>=0 and j<n:
            if chessboard[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True 

    def solveNQueens(self, n):
        ret = []
        chessboard = ["." * n for _ in range(n)]
        def backtracking(row):
            if row == n:
                ret.append(chessboard.copy())
                return
            for col in range(n):
                if not self.isValid(chessboard, row, col, n):
                    continue
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col+1:]
                backtracking(row+1)
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col+1:]
            
        backtracking(0)
        return ret
