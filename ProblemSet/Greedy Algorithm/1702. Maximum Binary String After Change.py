class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        z_idx = binary.find("0")
        if z_idx < 0:
            return binary
        p_cnt = binary.count("1", z_idx) # the number of "1" in binary[i:]
        return "1" * (len(binary)-1-p_cnt) + "0" + "1" * p_cnt
   