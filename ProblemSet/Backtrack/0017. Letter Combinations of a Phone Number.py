class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #Define a map
        ret = []
        map = {"2":["a", "b", "c"],
               "3":["d", "e", "f"],
               "4":["g", "h", "i"],
               "5":["j", "k", "l"],
               "6":["m", "n", "o"],
               "7":["p", "q", "r", "s"],
               "8":["t", "u", "v"],
               "9":["w", "x", "y", "z"]}

        def backtrack(comb, next_digits):
            # Base case
            if not next_digits:
                ret.append(comb) # some combination
            # Recursion
            else:
                for char in map[next_digits[0]]:
                    backtrack(comb+char, next_digits[1:])
        if digits:
            orig = ""
            backtrack(orig, digits)
        return ret
    ''' 
    # Similarly
    class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        n = len(digits)
        path = [""] * n
        def dfs(i):
            if i == n:
                ans.append("".join(path))
                return
            for c in mapping[int(digits[i])]:
                path[i] = c 
                dfs(i+1)
        
        if n > 0:
            dfs(0)
        return ans
    '''