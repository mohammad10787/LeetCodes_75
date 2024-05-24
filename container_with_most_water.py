class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        area = 0

        while left < right:
            tmp = min(height[left], height[right]) * (right - left)
            if tmp > area:
                area = tmp
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return area

if __name__ == '__main__':
    s = Solution()
    height = [2,3,10,5,7,8,9]
    print(s.maxArea(height))
