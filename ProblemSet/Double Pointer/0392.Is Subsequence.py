class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        ptr1, ptr2 = 0, 0
        while ptr1 <= len(s) - 1 and ptr2 <= len(t)-1:
            if s[ptr1] == t[ptr2]:
                ptr1 += 1
                ptr2 += 1
            else:
                ptr2 += 1
        if ptr1 == len(s):
            return True
        else:
            return False
        '''
        # Dp Method
        n1, n2 = len(s)+1, len(t)+1
        dp = [[0] * n2 for _ in range(n1)]
        for i in range(1, n1):
            for j in range(1, n2):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return True if dp[-1][-1] == len(s) else False

        '''
