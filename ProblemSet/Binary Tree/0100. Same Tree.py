# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case
        if not p or not q:
            return p == q
        leftside = self.isSameTree(p.left, q.left)
        rightside = self.isSameTree(p.right, q.right)
        return p.val == q.val if leftside and rightside else False
        