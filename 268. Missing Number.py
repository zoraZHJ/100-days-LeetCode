class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        count = [0] * n
        