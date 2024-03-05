class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            zeroCnt = s.count("0")
            oneCnt = s.count("1")
            for i in range(m, zeroCnt-1, -1):
                for j in range(n, oneCnt-1, -1):
                    # State transition compression equation
                    dp[i][j] = max(dp[i][j], dp[i-zeroCnt][j-oneCnt]+1)
        #print(dp)
        return dp[-1][-1]
