# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    def findIdx(self, value: int, l: List[int]) -> int:
        for i in range(len(l)):
            if l[i] == value:
                return i
    '''
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Base Case
        if len(postorder) == 0:
            return
        rootValue = postorder[-1]
        root = TreeNode(rootValue)
        if len(postorder) == 1:
            return root
        # Recursion
        #idx = self.findIdx(rootValue, inorder)
        idx = inorder.index(rootValue)
        l_inorder, r_inroder = inorder[:idx], inorder[idx+1:]
        l_postorder, r_postorder = postorder[:len(l_inorder)] ,postorder[len(l_inorder): len(postorder)-1]
        root.left = self.buildTree(l_inorder, l_postorder)
        root.right = self.buildTree(r_inroder, r_postorder)
        return root
