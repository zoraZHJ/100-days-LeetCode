class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n == -1:
            return 1.0/x
        
        half_n = int(n/2)
        half = self.myPow(x, half_n)
        if n % 2 == 1: #odd
            return half * half * self.myPow(x, n - half_n * 2)
        elif n % 2 == 0: #even
            return half * half