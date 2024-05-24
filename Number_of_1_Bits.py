class Solution:
    def hammingWeight(self, n):
        h = 0
        while n > 1:
            h = h + n % 2
            n = n // 2
        if n == 1:
            h += 1
        return h

if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(2147483645))