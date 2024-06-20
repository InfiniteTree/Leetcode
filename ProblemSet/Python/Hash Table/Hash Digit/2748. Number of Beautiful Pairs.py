class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        res = 0
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if gcd(int(str(nums[i])[0]), nums[j]%10) == 1:
                    res += 1
        '''
        # Optimization: Hash Table
        cnt = [0] * 10 # Store the times of num[0] from 1 - 9
        for x in nums:
            for y in range(10):
                if gcd(y, x%10) == 1:
                    res += cnt[y]
            while x >= 10:
                x //= 10
            cnt[x] += 1
        return res
