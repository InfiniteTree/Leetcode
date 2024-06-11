class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # dp[i][j] whether can reach the (i,j) starting from the first Column
        m, n = len(grid) ,len(grid[0])
        dp = [[False] * n for _ in range(m)]
        maxMove = 0

        for i in range(m):
            dp[i][0] = True

        for j in range(1, n):
            for i in range(m):
                for dir in range(-1, 2): # move from -1, 0, 1
                    if i+dir<0 or i+dir>=m:
                        continue
                    if grid[i][j] > grid[i+dir][j-1] and (j == 1 or dp[i+dir][j-1]):
                        dp[i][j] = True
                        maxMove = j
                        break
        #print(dp)
        return maxMove
