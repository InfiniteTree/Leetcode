class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = ""
        def backtracking(l, r, path):
            if l == 0 and r == 0:
                res.append(path)
                return
            elif l > r:
                return
            
            if l > 0:
                backtracking(l-1, r, path+"(")
            if r > 0:
                backtracking(l, r-1, path+")")
            return
        backtracking(n, n, path)
        return res
