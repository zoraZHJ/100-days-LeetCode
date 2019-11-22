class Solution:
    def myAtoi(self, str: str) -> int:
        valid_begin = False
        is_signed = False
        res = 0
        for s in str:
            if not valid_begin:
                if s == ' ':
                    continue
                elif s >= '0' and s <= '9':
                    valid_begin = True
                    res = int(s)
                elif s == '-':
                    valid_begin = True
                    is_signed = True
                elif s == '+':
                    valid_begin = True
                else:
                    return 0
            elif valid_begin:
                if s >= '0' and s <= '9':
                    res = res * 10 + int(s)
                else:
                    break
        res = -res if is_signed else res
        res = (2**31-1) if res > (2**31-1) else res
        res = -(2**31) if res < -(2**31) else res
        
        return res
            