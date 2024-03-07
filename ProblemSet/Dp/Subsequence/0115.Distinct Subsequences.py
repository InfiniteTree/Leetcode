class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1, n2 = len(s)+1, len(t)+1
        # Initialization
        dp = [[0] * n2 for _ in range(n1)] # dp[i][j] indicates the number of t[:j-1] appear in the s[:i-1]
        for i in range(n1): # t == ""
            dp[i][0] = 1
        
        # Recursion
        # example: s = "babgbag", t = "bag"
        for i in range(1, n1):
            for j in range(1, n2):
                if s[i-1] == t[j-1]: # i.e :"g"
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j] # the number of "ba" + the number of "bag"
                else:
                    dp[i][j] = dp[i-1][j] # the number of "bag" 
        # print(dp)
        return dp[-1][-1] 
