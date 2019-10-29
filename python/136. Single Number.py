class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        len_num = len(nums)
        if len_num % 2 == 0:
            return -1
        res = 0
        for num in nums:
            res = res ^ num
        return res
