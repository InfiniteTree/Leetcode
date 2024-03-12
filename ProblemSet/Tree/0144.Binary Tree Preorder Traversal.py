# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    def traversal(self, cur: Optional[TreeNode], res) -> List[int]:
        if not cur:
            return
        res.append(cur.val)
        self.traversal(cur.left, res)
        self.traversal(cur.right, res)
    '''
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        '''
        self.traversal(root, res) # Recursion Method
        '''
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            if cur:
                res.append(cur.val)
            else:
                continue
            # Notice that the pop func will pop left node first with the FILO stack
            if cur.left:
                stack.append(cur.right)
            if cur.right:
                stack.append(cur.left)
        return res
