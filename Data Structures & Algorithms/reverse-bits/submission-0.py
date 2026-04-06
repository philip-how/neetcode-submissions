class Solution:
    def reverseBits(self, n: int) -> int:
        rolling_num = 0
        for i in range(32):
            rolling_num |= ((n >> i) & 1) << (32-i-1)
        return rolling_num