class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        save_idx = 0
        access_idx = 1
        while(access_idx < len_nums):
            if nums[access_idx] != nums[save_idx]:
                nums[save_idx] = nums[access_idx]
                save_idx += 1
            access_idx += 1
        return save_idx+1