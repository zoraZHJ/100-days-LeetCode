class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        count = [0] * n
        for num in nums:
            count[num] = 1
        for i in range(n):
            if count[i] == 0:
                return i
                break