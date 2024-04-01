class Solution:
    def finalString(self, s: str) -> str:
        '''
        # Simulation
        res = ""
        for char in s:
            if char != "i":
                res += char
            else:
                res = res[::-1]
        return res
        '''
        # double-end queue
        q = deque()
        tail = True
        for c in s:
            if c == "i":
                tail = not tail
            else:
                if tail: # do not append i
                    q.append(c)
                else:
                    q.appendleft(c)
        res = "".join(q)
        return res if tail else res[::-1] 
