class Solution:
    def reverseBits(self, n: int) -> int:
        count = 0
        for i in range(32):
            count = (count << 1) | (n & 1)
            n >>= 1
        return count

