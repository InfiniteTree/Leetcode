class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cnt = sum(char.isupper() for char in word)
        return cnt == 0 or cnt == len(word) or (cnt == 1 and word[0].isupper())
