class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        for x in zip(*strs):
            x_set = set(x)
            if len(x_set) == 1:
                common += x[0]
            else:
                break
        return common
