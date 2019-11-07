class Solution:
    def rob(self, nums: List[int]) -> int:
        len_num = len(nums)
        if(len_num == 0):
            return 0

        dp = []
        dp.append(nums[0])
        
        #initilize status
        if(len_num == 1):
            return dp[-1]

        if(len_num > 1):
            dp.append(max(dp[-1], nums[1]))
        
        # status function
        for i in range(2, len_num):
            max_before = 0
            for j in range(i-1):
                max_before = max(max_before, dp[j] + nums[i])
            dp.append(max_before)

        return max(dp[-1], dp[-2])