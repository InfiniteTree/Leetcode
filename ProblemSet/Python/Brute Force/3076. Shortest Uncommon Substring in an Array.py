class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        def check(i: int, sub :str) -> bool:
            for j, s in enumerate(arr):
                if j != i and sub in s:
                    return False
            return True
        ans = []
        for i, s in enumerate(arr):
            res = ""
            for size in range(1, len(s)+1):
                for j in range(size, len(s)+1):
                    t = s[j-size: j]
                    if not res or t < res:
                        if check(i, t):
                            res = t
                if res: 
                    break
            ans.append(res)
        return ans
