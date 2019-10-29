class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        len_s = len(s)
        j = len_s - 1
        res = True
        while( i<j and i<len_s and j >= 0):
            while( not s[i].isalnum() ):
                i += 1
                if i >= len_s:
                    break
            while( not s[j].isalnum() ):
                j -= 1
                if j < 0:
                    break
                    
            if i<j:
                if s[i].lower() != s[j].lower():
                    res = False
                    break
                else:
                    i += 1
                    j -= 1
        
        return res