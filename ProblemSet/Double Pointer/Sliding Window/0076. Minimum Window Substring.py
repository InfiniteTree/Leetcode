from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        need = len(t)
        l = r = 0
        res = [0, inf]

        while r <= len(s)-1:
            if s[r] in t_counter:
                if t_counter[s[r]] > 0:
                    need -= 1
                t_counter[s[r]] -= 1
                
                # Here we can begin to shift the window
                while need == 0:
                    if r - l < res[1] - res[0]: # Update result
                        res = [l, r]
                    
                    # Move the left Pointer until it reach a neccessary element in t_counter
                    if s[l] in t_counter:
                        if t_counter[s[l]] == 0:
                            need += 1 # add the need back
                        t_counter[s[l]] += 1
                    l += 1
            r += 1
        return s[res[0]:res[1]+1] if res[1] != inf else ""
