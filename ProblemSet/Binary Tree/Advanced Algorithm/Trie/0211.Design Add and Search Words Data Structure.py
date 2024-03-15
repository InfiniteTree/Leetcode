class Node:
    def __init__(self):
        self.isEnd = False
        self.next = collections.defaultdict(Node) 
class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            # Get the index of the char
            cur = cur.next[c]
        cur.isEnd = True

    def match(self, word: str, idx: int, cur: Optional[Node]) -> bool:
        if cur == None:
            return False
        if idx == len(word):
            return cur.isEnd

        char = word[idx]
        if char != ".":
            return self.match(word, idx+1, cur.next.get(char))
        else:
            for child in cur.next.values():
                if self.match(word, idx+1, child):
                    return True
        return False 

    def search(self, word: str) -> bool:
        return self.match(word, 0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)