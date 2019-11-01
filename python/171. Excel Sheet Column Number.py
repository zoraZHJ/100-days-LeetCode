class Solution:
    def titleToNumber(self, s: str) -> int:
        num = 0
        for letter in s:
            n_tmp = ord(letter) - ord('A') + 1
            num = num * 26 + n_tmp
        return num
