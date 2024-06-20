from decimal import Decimal
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        chars = sentence.split(" ")
        for i, char in enumerate(chars):
            flag = False # A flag to judge whether it is a price
            if char[0] == "$" and len(char) > 1:
                flag = True
                x = 0
                for j in range(1, len(char)):
                    if char[j].isdigit():
                        x = x*10 + int(char[j])
                    else:
                        flag = False
                        break
                if flag:
                    x = x*(1-discount/100)
                    x = Decimal(x).quantize(Decimal("0.00"))
                    chars[i] = "$" + str(x)
        res = " ".join(chars)
        return res
        '''
        # Reference Answer
        arr = sentence.split(' ')
        res = []
        for i in arr:
            if i[0] == '$' and i[1:].isdigit():
                # print(int(i[1:])*(100-discount)/100)
                i = f"${(int(i[1:])*(100-discount)/100):.2f}"
            res.append(i)
        return ' '.join(res)
        '''