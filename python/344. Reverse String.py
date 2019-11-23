class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_s = len(s)
        half_len_s = len_s // 2
        for i in range(half_len_s):
            tmp = s[i]
            s[i] = s[len_s - i]
            s[len_s - i] = tmp