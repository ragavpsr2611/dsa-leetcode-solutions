"""
LeetCode 643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/

Pattern: sliding window (fixed size)

Time:  O(n)  - the first window costs k, then each of the remaining n - k
               slides is one addition and one subtraction: k + (n - k) = n
Space: O(1)  - the first window is summed with a loop, so no slice copy is made
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        a = len(nums)
        total = 0
        for i in range(k):
            total += nums[i]
        maxavg = float(total) / k
        for i in range(k, a):
            total += nums[i]
            total -= nums[i - k]
            avg = float(total) / k
            maxavg = max(maxavg, avg)
        return maxavg
