from typing import List

# a nice idea is to use the sum of the list without the missing number and subtract it from num.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        Sum = n*(n+1)/2
        for element in nums:
            Sum -= element
        return Sum


if __name__ == '__main__':
    s = Solution()
    nums = [3,0,1]
    print(s.missingNumber([3,0,1]))