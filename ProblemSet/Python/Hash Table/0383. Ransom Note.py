class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = [0] * 26
        for char in magazine:
            idx = ord(char) - ord("a")
            hash_map[idx] += 1
        for char in ransomNote:
            idx = ord(char) - ord("a")
            hash_map[idx] -= 1
        for num in hash_map:
            if num < 0:
                return False
        return True
        