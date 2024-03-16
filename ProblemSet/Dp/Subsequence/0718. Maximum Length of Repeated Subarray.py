class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 <= 1 or n2 <= 1:
            return 1 if nums1[0] == nums2[0] else 0
        dp = [[0] * (n2+1) for _ in range(n1+1)] # dp[i][j] indicates to nums1[i-1] and nums2[j-1]
        result = 0
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > result:
                    result = dp[i][j]
        # print(dp)
        return result
