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
        self.traversal(cur.left, res)
        res.append(cur.val)
        self.traversal(cur.right, res)
    '''

    '''
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        ### self.traversal(root, res) # Recursion Method
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur) # Access: push the node into the stack
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val) # Deal: do operation on the cur node
                cur = cur.right
        return res
    '''
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
                stack.extend([cur, None])
                if cur.left:
                    stack.append(cur.left)
            
        return res

