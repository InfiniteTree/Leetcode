# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def rightSide(node, depth):
            if node is None:
                return
            if depth == len(ret):
                ret.append(node.val)
            rightSide(node.right, depth+1)
            rightSide(node.left, depth+1)
        rightSide(root, 0)
        return ret
