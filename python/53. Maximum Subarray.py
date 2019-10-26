class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_sum = nums[0]
        partial_sum = nums[0]
        for num in nums[1:]:
            if partial_sum < 0:
                partial_sum = num
            else:
                partial_sum = partial_sum + num
            max_sum = partial_sum if partial_sum > max_sum else max_sum
        return max_sum