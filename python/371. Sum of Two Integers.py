import sys
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while(a & 0xFFFFFFFF != 0):
            carry = (a & b)
            b = (a ^ b)
            a = carry << 1
        sum = b if a<=0xFFFFFFFF else (b & (0xFFFFFFFF))
        return sum

if __name__ == '__main__':
    sln =Solution()

    # sum = sln.getSum(-1, 1)
    sum = sln.getSum(-31, 54)
    # sum = sln.getSum(-12, -8)
    print(sum)