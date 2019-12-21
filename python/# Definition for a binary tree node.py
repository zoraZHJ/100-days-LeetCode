# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if(root == None):
            return root
        if(root.val > key):
            root.left = self.deleteNode(root.left, key)
        elif(root.val < key):
            root.right = self.deleteNode(root.right, key)
        elif(root.left is not None and root.right is not None):
            root.val = self.findMin(root.right).val
            root.right = self.deleteNode(root.right, root.val)
        else:
            root = root.left if (root.left is not None) else root.right
        return root

    def findMin(self, root: TreeNode):
        if root is None:
            return root
        else:
            res = root
            while(res.left):
                res = res.left
        return res


