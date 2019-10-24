class Solution:
    def reverse(self, x: int) -> int:
        is_signed = True if x >= 0 else False
        x = abs(x)
        div_v = int(x / 10)
        mod_v = x % 10
        print(div_v)
        
        res = 0
        while(div_v!=0):
            res = res * 10 + mod_v
            if res > (2**31-1) or res <= (-2**31-1):
                return 0
            x = div_v
            div_v = int(x / 10)
            mod_v = x % 10
        res = res * 10 + mod_v
        if res > (2**31-1) or res <= (-2**31-1):
            return 0
        if not is_signed:
            res = -res
        return res
    
if __name__ == '__main__':
    sln = Solution()
    res = sln.reverse(123)
    print(res)