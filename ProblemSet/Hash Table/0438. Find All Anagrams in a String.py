class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        res = []
        if s_len < p_len: return res
        
        p_cnt = [0] * 26
        s_cnt = [0] * 26
        for char in p:
            idx = ord(char) - ord("a")
            p_cnt[idx] += 1
        
        left = 0
        for right in range(s_len):
            right_idx = ord(s[right]) - ord("a")
            s_cnt[right_idx] += 1
            while s_cnt[right_idx] > p_cnt[right_idx]:
                left_idx = ord(s[left]) -ord("a")
                s_cnt[left_idx] -= 1
                left += 1
            if right - left + 1 == p_len:
                res.append(left)
        return res
