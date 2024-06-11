class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res = 0
        happiness.sort(reverse=True)
        for i in range(len(happiness)):
            happiness[i] = max(happiness[i]-i, 0)
            res += happiness[i]
            if i == k-1:
                return res
            