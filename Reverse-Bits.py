class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res


if __name__ == "__main__":
    s = Solution()
    n = 0b00000010100101000001111010011100
    print(s.reverseBits(n))
