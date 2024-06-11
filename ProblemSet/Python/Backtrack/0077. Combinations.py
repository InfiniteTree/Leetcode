class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def backtracking(idx):
            if len(path) == k:
                res.append(path.copy())
                return
            for i in range(idx, n+1):
                path.append(i)
                backtracking(i+1)
                path.pop()
        backtracking(1)
        return res

                