class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_t = "".join(c.lower() for c in s if c.isalnum())
        return s_t == s_t[::-1]
