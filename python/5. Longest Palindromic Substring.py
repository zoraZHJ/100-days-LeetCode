class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        if len_s == 0:
            return ''

        dp = [[1 if i == j else 0 for i in range(len_s)] for j in range(len_s)]
        longestStr = s[0]
        if len_s == 1:
            return longestStr
        
        #len==2
        for i in range(len_s-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 2
                longestStr = s[i:i+2]
            else:
                dp[i][i+1] = 0
        #len=[3:len_s]
        for len_p in range(3, len_s+1):
            for i in range(len_s-len_p+1): #start point
                j = i + len_p - 1          #end point
                if s[i] == s[j] and dp[i+1][j-1] > 0:
                    dp[i][j] = dp[i+1][j-1] + 2
                    longestStr = s[i:j+1]
        
        return longestStr