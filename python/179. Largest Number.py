class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def get_bits(a):
            bits = 1
            while int(a / 10) != 0:
                a = int(a / 10)
                bits += 1
            return bits
        
        def compare(a, b):
            bits_a = get_bits(a)
            bits_b = get_bits(b)
            if ((a * (10**bits_b)) + b) > ((b * (10**bits_a)) + a):
                return True
            else:
                return False

        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(len_nums-i-1):
                if not compare(nums[j], nums[j+1]):
                    tmp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = tmp
        res = ""
        for i in range(len_nums):
            res += str(nums[i])
        if res[0] == "0":
            res = "0"
        return res