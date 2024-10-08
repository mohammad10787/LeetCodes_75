#You are given an array prices where prices[i] is the price of a given stock on the ith day.

#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# this is a test
class Solution:
    def maxProfit(self, prices):

        profit = 0

        left = prices[0]
        for index in range(len(prices) - 1):
            right = prices[index + 1]

            if right > left:
                if right - left > profit:
                    profit = right - left

            else:
                left = right

        return profit

        return max_price - min_price

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    S = Solution()
    profit = S.maxProfit(prices)
    print(profit)
