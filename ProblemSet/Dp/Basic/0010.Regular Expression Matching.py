class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s)+1, len(p)+1
        # Initiliazation
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
        
        # Dynamic processing    
        for i in range(1,m):
            for j in range(1, n):        
                if p[j-1] != "*":
                    if dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == "."):
                        dp[i][j] = True
                else:
                    if dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == ".")):
                        dp[i][j] = True
        return dp[-1][-1]
    