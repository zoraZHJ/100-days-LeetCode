class Solution:
    def twoSum(self, nums, target: int):

        for idx1, elt1 in enumerate(nums):
            tar_2 = target - elt1
            for idx2, elt2 in enumerate(nums[idx1+1:]):
                if elt2 == tar_2:
                    return [idx1, idx2+idx1+1]
            
        return []

if __name__ == '__main__':
    sln = Solution()
    res = sln.twoSum([3,2,4], 6)
    print(res)
        