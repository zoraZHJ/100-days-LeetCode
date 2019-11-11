class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        bit_idx = 0
        while(bit_idx < 32):
            print(hex(n))
            n = n & 0xffffffff
            bit = n & 0x1
            res = (res << 1) + bit
            n = (n >> 1) & 0xffffffff
            print("res:",hex(res))
            bit_idx += 1
        return res
        