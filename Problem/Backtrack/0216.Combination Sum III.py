class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        l = 9 # number 1 to 9
        path = []
        ret = []
        sum_val = 0
        start_val = 1
        def backtracking(startIdx, sum_val):
            if len(path) == k:
                if sum_val == n:
                    ret.append(path.copy())
                return

            for i in range(startIdx, l-(k-len(path))+1+1): 
                sum_val += i
                path.append(i)
                backtracking(i+1, sum_val)
                sum_val -= i
                path.pop()
                
        backtracking(start_val, sum_val)
        return ret
