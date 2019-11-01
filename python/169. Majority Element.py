class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_ele = nums[0]
        count = 1
        for num in nums[1:]:
            if maj_ele == num:
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    maj_ele = num
                    count = 1
        if count > 0:
            return maj_ele

