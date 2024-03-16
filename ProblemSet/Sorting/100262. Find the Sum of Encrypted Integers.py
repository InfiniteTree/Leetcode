class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            s = [int(ch) for ch in str(num)]
            ans += int(str(max(s)) * len(s))
        return ans