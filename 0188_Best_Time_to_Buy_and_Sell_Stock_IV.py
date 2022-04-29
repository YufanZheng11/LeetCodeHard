"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0)
and sell on day 6 (price = 3), profit = 3-0 = 3.


Constraints:

0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
"""

from functools import lru_cache


class Solution:

    def maxProfit(self, k, prices):
        """
        State:
            i: ith day
            s: state: 0 - buy, 1 - sell
            k: remaining transactions
        """

        # @lru_cache
        # def helper(i, s, k):
        #     if i == len(prices):
        #         return 0
        #     if k == 0:
        #         return 0
        #     # buy / sell
        #     if s == 0:
        #         do_something = -prices[i] + helper(i+1, 1, k)
        #         do_nothing = helper(i+1, 0, k)
        #         return max(do_nothing, do_something)
        #     else:
        #         do_something = prices[i] + helper(i+1, 0, k-1)
        #         do_nothing = helper(i+1, 1, k)
        #         return max(do_nothing, do_something)
        #
        # return helper(0, 0, k)

        n = len(prices)
        cache = [[[0] * (k+1) for _ in range(2)] for _ in range(n+1)]

        for o in range(1, k+1):
            for i in range(n-1, -1, -1):
                cache[i][0][o] = max(cache[i+1][1][o]-prices[i], cache[i+1][0][o])
                cache[i][1][o] = max(cache[i+1][0][o-1]+prices[i], cache[i+1][1][o])

        return cache[0][0][-1]
