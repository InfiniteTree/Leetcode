class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # the effect of deletion is the same as an insertion
        n1, n2 = len(word1)+1, len(word2)+1
        
        dp = [[0] * n2 for _ in range(n1)]
        for i in range(n1):
            dp[i][0] = i
        for j in range(n2):
            dp[0][j] = j
        
        for i in range(1, n1):
            for j in range(1, n2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        return dp[-1][-1]
