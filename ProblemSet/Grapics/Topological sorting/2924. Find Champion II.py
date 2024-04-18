class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        degs = [0] * n
        for u, v in edges:
            degs[v] += 1
        if degs.count(0) > 1: return -1
        return degs.index(0)
