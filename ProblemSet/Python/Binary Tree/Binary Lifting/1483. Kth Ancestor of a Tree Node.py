class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        m = n.bit_length()-1
        ances = [[p] + [-1] * m for p in parent]
        #print(ances)
        for i in range(m):
            for x in range(n):
                if (p := ances[x][i]) != -1:
                    ances[x][i+1] = ances[p][i]
        self.ances = ances
        #print(self.ances)

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if (k>>i) & 1:
                node = self.ances[node][i]
                if node < 0: break
        return node

              


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)