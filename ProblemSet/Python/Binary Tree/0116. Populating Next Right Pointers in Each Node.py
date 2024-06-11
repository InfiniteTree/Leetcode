"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #res = []
        if not root:
            return root
        q = deque([root])
        while q:
            #one_level = []
            path = []
            for _ in range(len(q)):
                cur = q.popleft()
                path.append(cur)
                #one_level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            for i in range(len(path)-1):
                path[i].next = path[i+1]
            path[-1].next = None
            #one_level.append("#")
            #res.extend(one_level)
        return root
