# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, cur: Optional[TreeNode]) -> int:
        if not cur:
            return 0
        if not cur.left and cur.right:
            return 1 + self.getHeight(cur.right)
        elif not cur.right and cur.left:
            return 1 + self.getHeight(cur.left)
        else:
            return 1 + min(self.getHeight(cur.left), self.getHeight(cur.right))

    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.getHeight(root)
