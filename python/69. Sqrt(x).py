class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        while(res*res<=x):
            res = res + 1
        return res-1