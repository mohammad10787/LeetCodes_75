# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums):
        HashMap = {}
        for index, element in enumerate(nums):
            if element in HashMap:
                return True

            else:
                HashMap[element] = index

        return False

if __name__ == '__main__':
    nums = [1,2,3,1]
    S = Solution()
    value = S.containsDuplicate(nums)
    print(value)