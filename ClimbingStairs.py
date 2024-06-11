class Solution:
    def climbStairs(self, n): # the solution is actually the Fibunaci series
        one, two = 1, 1
        for i in range(n-1):
            tmp = one
            one = one + two
            two = tmp
        return one


if __name__ == '__main__':
    s = Solution()
    n = 5
    print(s.climbStairs(n))