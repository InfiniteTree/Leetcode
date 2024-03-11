# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Function traversal:
    # return 0 if the node is not covered, 1 if covered but does not holds camera, 2 if holds camera    
    def traversal(self, root:Optional[TreeNode], camera:List) -> int:
        if not root:
            return 1 # to let the father node of the leaves node holds camera
        left = self.traversal(root.left, camera)
        right = self.traversal(root.right, camera)
        if left == 0 or right == 0: # neither of children is covered
            camera[0] += 1
            return 2
        if left == 2 or right == 2: # if any child holds carmera
            return 1
        if left == 1 and right == 1: # both of the children are coverd but does not holds camera
            return 0
    
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        camera = [0]
        if self.traversal(root, camera) == 0:
            camera[0] += 1
        return camera[0]
        