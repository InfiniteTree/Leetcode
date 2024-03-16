# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val == key:
            if not root.left and not root.right:
                return
            elif root.left and not root.right:
                return root.left
            elif root.right and not root.left:
                return root.right
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                return root.right
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        return root

    '''
    # Delete a Node in a normal tree instead of a BST
    # Swap it with a leaf node, delete it with None(after swapping its right child is None)  
        def deleteNode(self, root, key):
        if root is None: 
            return root
        if root.val == key:  
            if root.right is None:  
                return root.left
            cur = root.right
            while cur.left:  # Find the most left nodes of its right subtree
                cur = cur.left
            root.val, cur.val = cur.val, root.val  # swap the target val with the most left node val of the right subtree
        root.left = self.deleteNode(root.left, key)  
        root.right = self.deleteNode(root.right, key) 
        return root 
    '''