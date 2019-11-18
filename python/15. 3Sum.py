class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        len_num = len(nums)
        res = set()
        for i in range(len_num):
            j = i + 1
            k = len_num-1
            target_sum = - nums[i]
            while(j<k):
                tmp_sum = nums[j] + nums[k]
                if tmp_sum == target_sum:
                    res.add((nums[i], nums[j], nums[k]))
                    j = j + 1
                elif tmp_sum > target_sum:
                    k = k - 1
                elif tmp_sum < target_sum:
                    j = j + 1
        
        return res