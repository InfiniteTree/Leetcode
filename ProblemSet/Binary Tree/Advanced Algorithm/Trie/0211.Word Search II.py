class TrieNode:
    def __init__(self):
        self.s = None
        #self.next = collections.defaultdict(TrieNode)
        self.next = [None] * 26

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.board = None
        self.m = 0
        self.n = 0
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.visited = None
        self.res = set()

    def BuildTrie(self, words: List[str]) -> None:
        for word in words:
            cur = self.root
            for char in word:
                #cur = cur.next[char]
                idx = ord(char) - ord("a")
                if not cur.next[idx]: 
                    cur.next[idx] = TrieNode()
                cur = cur.next[idx]
            cur.s = word

    def dfs(self, i: int, j: int, cur: Optional[TrieNode]) -> None:
        if cur.s:
            self.res.add(cur.s)
        for d in self.dirs:
            y, x = i + d[1], j + d[0]
            if x < 0 or y < 0 or x >= self.n or y >= self.m:
                continue
            if self.visited[y][x]:
                continue
            char = self.board[y][x]
            idx = ord(char) - ord("a")
            if cur.next[idx]:
                self.visited[y][x] = True
                self.dfs(y, x, cur.next[idx])
                self.visited[y][x] = False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.BuildTrie(words)
        self.board = board
        self.m, self.n = len(board), len(board[0])
        self.visited = [[False] * (self.n+1) for _ in range(self.m+1)]
        #self.visited = [[False] * 16 for _ in range(16)]
        cur = self.root
        for i in range(self.m):
            for j in range(self.n):
                char = self.board[i][j]
                idx = ord(char) - ord("a")
                if cur.next[idx]:
                    self.visited[i][j] = True
                    self.dfs(i, j, cur.next[idx])
                    self.visited[i][j] = False  
        return list(self.res)
