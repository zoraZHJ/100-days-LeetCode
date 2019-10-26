class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        for num in digits[-1::-1]:
            num = num + carry
            if num >= 10:
                num = 0
                carry = 1
            else:
                carry = 0
            res.insert(0, num)
        if carry == 1:
            res.insert(0, carry)
        return res
