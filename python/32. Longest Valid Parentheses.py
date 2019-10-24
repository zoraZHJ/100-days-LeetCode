class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0 or n == 1:
            return 0
        
        dp = 0
        tmp_dp = 0
        max_len = 0
        tmp_s = s[0] if s[0] == '(' else ''

        for i in range(1, n):
            if s[i] == ')' and len(tmp_s) == 0:
                max_len = max_len if max_len >= dp else dp
                dp = 0
            elif s[i] == ')' and tmp_s[-1] == '(':
                tmp_dp = tmp_dp + 2
                tmp_s = tmp_s[0:-1]
                if len(tmp_s) == 0:
                    dp = dp + tmp_dp
                    tmp_dp = 0
            elif s[i] == '(':
                tmp_s = tmp_s + s[i]
        if tmp_dp != 0:
            dp = tmp_dp
        max_len = max_len if max_len >= dp else dp
        return max_len

if __name__=='__main__':
    sln = Solution()
    # ()(()) 6
    # )()()) 4
    # (() 2
    res = sln.longestValidParentheses("(()(((()")
    print(res)
                