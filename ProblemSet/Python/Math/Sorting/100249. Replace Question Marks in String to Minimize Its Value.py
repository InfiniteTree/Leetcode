class Solution:
    def minimizeStringValue(self, s: str) -> str:
        res = ""
        cost = [0] * 26
        in_char = []
        for char in s:
            if char != "?":
                idx = ord(char) - ord("a")
                cost[idx] += 1
        
        for char in s:
            if char == "?":
                min_char = min(cost)
                in_idx = cost.index(min_char)
                in_char.append(chr(ord("a") + in_idx)) 
                cost[in_idx] += 1
        
        in_char.sort()
        i, j = 0, 0
        for char in s:
            if char == "?":
                res += in_char[j]
                j += 1
            else:
                res += char
            i += 1
        return res