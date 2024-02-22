class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank, cur, start = 0, 0, 0
        for i in range(n):
            tank += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                start = i+1
        return start if tank >= 0 else -1
            