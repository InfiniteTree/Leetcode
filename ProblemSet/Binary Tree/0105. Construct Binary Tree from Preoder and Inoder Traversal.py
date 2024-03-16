# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        cur = TreeNode(preorder[0]) # 确定前序遍历的首节点为当前遍历要构造的节点
        idx = inorder.index(cur.val) # 获取其在中序遍历数组中的位置，从而知道此节点的左右子树的划分
        cur.left = self.buildTree(preorder[1:idx+1], inorder[:idx]) # 遍历构造对应左子树 
        cur.right = self.buildTree(preorder[idx+1:], inorder[idx+1:]) # 遍历构造对应右子树 
        return cur
