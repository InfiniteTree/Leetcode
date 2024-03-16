# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
        self.kth = None

    def traversal(self, cur: Optional[TreeNode], k: int):
        if not cur:
            return

        self.kthSmallest(cur.left, k)
        if self.count == k: # pruning
            return
        self.count += 1
        if self.count == k:
                self.kth = cur.val
        self.kthSmallest(cur.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traversal(root, k)
        return self.kth
