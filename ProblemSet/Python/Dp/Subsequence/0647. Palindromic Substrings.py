class Solution:
    '''
    def countSubstrings(self, s: str) -> int:
        
        # dp[i][j]: whether s[i:j] is a palindromic substring
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        result = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j-i<=1:
                        dp[i][j] = True
                        result += 1
                    elif dp[i+1][j-1]:
                        dp[i][j] = True
                        result += 1
        return result
    '''
    # Double Pointers
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result += self.extend(s, i, i, len(s)) # use i as the center
            result += self.extend(s, i, i+1, len(s)) # use [i, i+1] as the center
        return result
    
    def extend(self, s, i, j, n):
        res = 0
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
            res += 1
        return res
     