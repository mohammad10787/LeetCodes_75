# Use HashMap to find two numbers that sum to target value
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
class Solution:

    def twoSum(self, nums, target: int):
        TwoSumMap = {}
        for index, element in enumerate(nums):
            if target - element in TwoSumMap:
                return [index, TwoSumMap[target - element]]

            TwoSumMap[element] = index

if __name__ == "__main__":
    S = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    arr = S.twoSum(nums, target)
    print(arr)