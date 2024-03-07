class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j]: whether s[i:j] is a palindrmoic substring
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        #dp[0][0] = True
        result = ""
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j-1 <= i:
                        dp[i][j] = True
                    elif dp[i+1][j-1]:
                        dp[i][j] = True
                if dp[i][j] and len(s[i:j+1]) > len(result):
                    result = s[i:j+1]
        '''
        for i in range(n):
            for j in range(n-1, -1, -1):
                if dp[i][j]:
                    result = s[i:j+1]
                    return result
        #print(dp)
        '''
        return result
    