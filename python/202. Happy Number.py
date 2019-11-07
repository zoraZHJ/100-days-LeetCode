class Solution:
    def isHappy(self, n: int) -> bool:
        max_count = 10
        
        idx = 0
        sum = 0
        
        while(sum!=1 and idx<max_count):
            sum = 0
            for num in str(n):
                sum += int(num) ** 2
            idx += 1
            n = sum
        return True if sum == 1 else False