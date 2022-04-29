"""
https://leetcode.com/problems/maximum-gap/

Given an integer array nums, return the maximum difference between two successive elements in its sorted form.
If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.


Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
"""


class Solution:

    def maximumGap(self, nums):
        """ Buckets """
        n = len(nums)
        if n < 2:
            return 0

        minVal, maxVal = min(nums), max(nums)
        bucketSize = float(maxVal - minVal) / (n - 1)

        if not bucketSize:
            return 0

        buckets = [[] for _ in range(n)]
        for num in nums:
            index = int((num - minVal) / bucketSize)
            if not len(buckets[index]):
                buckets[index] = [num, num]
            else:
                buckets[index][0] = min(num, buckets[index][0])
                buckets[index][1] = max(num, buckets[index][1])

        maxGap = 0
        preMax = None
        for bucket in buckets:
            if not bucket:
                continue
            if preMax is not None:
                maxGap = max(maxGap, bucket[0] - preMax)
            preMax = bucket[1]
        return maxGap
