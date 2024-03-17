from collections import Counter
#  The rule that once you reach a tree with fruit that cannot fit in your baskets, you must stop,
#  which require the subarray to be continue!!!
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = Counter()
        left, right, ans = 0, 0, 0
        while right < len(fruits):
            cnt[fruits[right]] += 1
            while len(cnt) > 2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    cnt.pop(fruits[left])
                left += 1
            ans = max(ans, right-left+1)
            right += 1
        return ans
