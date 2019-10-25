class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_stack = len(haystack)
        len_needle = len(needle)
        if len_needle == 0:
            return 0
        for stack_idx in range(len_stack - len_needle + 1):
            if haystack[stack_idx : stack_idx + len_needle] == needle:
                return stack_idx
        return -1