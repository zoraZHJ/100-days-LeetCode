class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        power_val = 1
        if(n==1):
            return True
        while(power_val<n):
            power_val = power_val * 3
            if power_val == n:
                return True
        
        return False