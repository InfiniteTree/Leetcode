class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        res = 0
        coins.sort()
        s, i = 1, 0
        while s <= target:
            if i < len(coins) and coins[i] <= s:
                s += coins[i]
                i += 1
            else:
                s += s # need to add s to the coins
                res += 1
        return res
        