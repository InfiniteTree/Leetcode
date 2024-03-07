class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp[i][j]: in the matrix[:i][:j] the length of edge of the larget square
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        result = 0
        for i in range(m):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                result = 1
        for j in range(n):
            if matrix[0][j] == "1":
                dp[0][j] = 1
                result = 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    if dp[i][j] >= result:
                        result = dp[i][j]
        return result**2 
                