class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 == 1: # odd array
            return []
        
        res = []
        cnt = Counter()
        changed.sort()
        
        for x in changed:
            if x not in cnt: # not the double element, which means the original
                cnt[x*2] += 1
                res.append(x)
            else: # the double elememt
                cnt[x] -= 1
                if cnt[x] == 0:
                    del cnt[x]
        return [] if cnt else res
