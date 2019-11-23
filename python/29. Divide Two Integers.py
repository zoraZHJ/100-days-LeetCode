class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        is_signed = (dividend < 0) ^ (divisor < 0)

        step = 1
        res = 0

        dividend = abs(dividend)
        divisor = abs(divisor)
        copy = divisor

        sum = 0
        max_range = pow(2, 31)
        while True:
            sum = sum + divisor
            res = res + step
            if sum > dividend:
                if step == 1:
                    res = res - 1
                    break
                sum = sum - divisor
                res = res - step
                step = step >> 1
                divisor = divisor >> 1
                
            else:
                divisor = divisor << 1
                step = step << 1

        res = -res if is_signed else res
        if res < -max_range:
            res = -max_range
        if res > (max_range - 1):
            res = max_range - 1
        
        return res