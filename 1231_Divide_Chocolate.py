"""
https://leetcode.com/problems/divide-chocolate/

You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your k friends so you start cutting the chocolate bar into k + 1 pieces using k cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.


Example 1:

Input: sweetness = [1,2,3,4,5,6,7,8,9], k = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
Example 2:

Input: sweetness = [5,6,7,8,9,1,2,3,4], k = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.
Example 3:

Input: sweetness = [1,2,2,1,2,2,1,2,2], k = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
"""

from functools import lru_cache


class Solution:
    def maximizeSweetness(self, sweetness, k: int) -> int:

        n = len(sweetness)

        prefixSum = []
        for sweet in sweetness:
            if not prefixSum:
                prefixSum.append(sweet)
            else:
                prefixSum.append(prefixSum[-1] + sweet)

        @lru_cache(None)
        def totalSweetness(i, j):
            if i == 0:
                return prefixSum[j]
            return prefixSum[j] - prefixSum[i - 1]

        @lru_cache(None)
        def helper(i, k):
            """
            States:
                - i: starting from ith
                - k: cuts needed
            """
            if k == 0:
                return totalSweetness(i, n - 1)
            maxSweet = 0
            for j in range(i + 1, n - k + 1):
                sweet = min(totalSweetness(i, j - 1), helper(j, k - 1))
                maxSweet = max(maxSweet, sweet)
            return maxSweet

        return helper(0, k)
