# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def traversal(self, cur: Optional[TreeNode]):
        if not cur:
            return
        
        self.convertBST(cur.right)
        cur.val += self.count
        self.count = cur.val
        self.convertBST(cur.left)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traversal(root)
        return root
        