class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ori_len = len(nums)
        while 0 in nums:
            nums.remove(0)
        after_len = len(nums)
        zero_num = ori_len - after_len
        nums.extend(zero_num*[0])