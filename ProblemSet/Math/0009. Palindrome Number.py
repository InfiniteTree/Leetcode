class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        return strX == strX[::-1]
