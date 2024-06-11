from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a >= c:
                    dp[a] = min(dp[a], dp[a-c] + 1)
        return dp[amount] if dp[amount] <= amount else -1


if __name__ == '__main__':
    s = Solution()
    amount = 7
    coins = [1, 3, 4, 5]
    print(s.coinChange(coins, amount))