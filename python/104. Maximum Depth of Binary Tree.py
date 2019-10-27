# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        max_depth_left = self.maxDepth(root.left)
        max_depth_right = self.maxDepth(root.right)
        max_depth = max_depth_left if max_depth_left > max_depth_right else max_depth_right
        max_depth += 1
        return max_depth
        