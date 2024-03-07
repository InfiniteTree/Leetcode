class Solution:
    def isValid(self, chessboard, row, col, n):
        for i in range(n):
            if chessboard[i][col] == "Q":
                return False
        
        i, j = row-1, col-1
        while i>=0 and j>=0:
            if chessboard[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        
        i, j = row-1, col+1
        while i>=0 and j<n:
            if chessboard[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True

    def totalNQueens(self, n: int) -> int:
        ret = 0
        chessboard = ["." * n for _ in range(n)]
        def backtracking(row):
            if row == n:
                nonlocal ret
                ret += 1
                return
            for col in range(n):
                if not self.isValid(chessboard, row, col, n):
                    continue
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col+1:]
                backtracking(row+1)
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col+1:]
            
        backtracking(0)
        return ret
