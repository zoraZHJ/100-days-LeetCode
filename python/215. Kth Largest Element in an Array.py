class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        len_nums = len(nums)
        for i in range(k):
            for j in range(len_nums - 1 - i):
                if nums[j] > nums[j+1]:
                    tmp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = tmp
        return nums[len_nums - k]
