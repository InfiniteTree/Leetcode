# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max = -1000

    def traversal(self, cur: Optional[TreeNode]):
        if not cur:
            return 0 
        
        left = max(self.traversal(cur.left), 0)
        right = max(self.traversal(cur.right),0)
        self.max = max(self.max, left+right+cur.val)
        return cur.val + max(left,right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.traversal(root)
        return self.max