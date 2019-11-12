class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        if len_s == 0:
            return 0
        dp = [1]
        if len_s == 1:
            return 1
        for i in range(1, len_s):
            sub_s = s[(i-dp[i-1]):i]
            if s[i] not in sub_s:
                dp.append(dp[i-1]+1)
            else:
                c_idx = sub_s.index(s[i])
                dp.append(dp[i-1]-c_idx)
        
        max_len = max(dp)
        
        return max_len
