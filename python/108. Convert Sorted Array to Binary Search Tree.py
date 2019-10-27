# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        len_nums = len(nums)
        if len_nums == 0:
            return None
        root_pos = len_nums // 2
        root = TreeNode(nums[root_pos])
        print(root_pos)
        
        root.left = self.sortedArrayToBST(nums[0:root_pos])
        if root_pos == len_nums - 1:
            root.right = None
        else:
            print(nums[root_pos+1:-1])
            root.right = self.sortedArrayToBST(nums[root_pos+1:])
        return root