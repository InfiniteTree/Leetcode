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

    '''
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        ###self.traversal(root, res) # Recursion Method
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                res.append(cur.val)
            else:
                continue
            # Notice that the pop func will pop left node first with the FILO stack
            stack.append(cur.right)
            stack.append(cur.left)
        return res
    '''
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        if cur:
            stack.append(cur)
        while stack:
            cur = stack.pop()
            if not cur: # the cur node is the None label for dealing
                cur = stack.pop()
                res.append(cur.val)
                continue
            else:
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
                stack.extend([cur, None])
        return res
