# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = None
        self.min_dif = float("inf") 
     # mindif will only appear within the cur.val and pre.val in a BST 
    def traversal(self, cur: Optional[TreeNode]) -> int:
        if not cur:
            return 
        self.getMinimumDifference(cur.left)
        if self.pre:
            self.min_dif = min(self.min_dif, abs(cur.val-self.pre.val))
        self.pre = cur 
        self.getMinimumDifference(cur.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.traversal(root)
        return self.min_dif
