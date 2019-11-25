class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def permute_single(nums, tmp_res):
            if len(nums) == 0:
                res.append(tmp_res[:])
                return
            else:
                for num in nums:
                    tmp_res.append(num)
                    tmp_list = nums[:]
                    tmp_list.remove(num)
                    permute_single(tmp_list, tmp_res)
                    tmp_res.pop()
        
        permute_single(nums, [])
        return res