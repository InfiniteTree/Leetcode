"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        q = deque([root])
        while q:
            length = len(q)
            path = []
            for _ in range(length):
                cur = q.popleft()
                path.append(cur.val)
                q.extend(cur.children)
            res.append(path)
        return res
        