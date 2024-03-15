# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The core idea here is to let the right child of the most right node in the left subtree of this root node points to the root
# which we call it predecessor, and then update the x to the x.left, coutinue doing this until all the node can find the predecessor
# so we use the null ptr of the leaves node instead of using a stack 
class Solution:
    def morris(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        predecessor = None
        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    predecessor.right = root
                    root = root.left
                else:
                    res.append(root.val)
                    predecessor.right = None
                    root = root.right
            else:
                res.append(root.val)
                root = root.right
        return res

