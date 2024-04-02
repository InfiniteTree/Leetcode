# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        res = []
        if n % 2 == 0: # False to construct
            return res
        if n == 1:
            res.append(TreeNode(0))
            return res
        
        for i in range(1, n, 2):
            left_trees = self.allPossibleFBT(i)
            right_trees = self.allPossibleFBT(n-1-i)
            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(0, left_tree, right_tree)
                    res.append(root)
        return res
        