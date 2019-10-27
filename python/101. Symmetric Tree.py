# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSymmetric(self, node1: TreeNode, node2: TreeNode) -> bool:
        if node1 == None and node2 == None:
            return True
        elif node1 == None or node2 == None:
            return False
        if node1.val != node2.val:
            return False
        return self.twoSymmetric(node1.left, node2.right) and self.twoSymmetric(node1.right, node2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.twoSymmetric(root.left, root.right)