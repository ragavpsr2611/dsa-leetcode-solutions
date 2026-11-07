"""
LeetCode 209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

Pattern: sliding window (variable size), SHORTEST valid window - the answer
         is recorded inside the shrink loop, while the window is still valid

Works only because all numbers are positive: adding an element never
decreases the sum and removing one never increases it, so the left pointer
never has to move back.

Time:  O(n)  - i moves right n times; l only moves right, at most n times
               in total
Space: O(1)  - a few integers
"""


class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        total = 0
        best = len(nums) + 1
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                best = min(best, i - l + 1)
                total -= nums[l]
                l += 1
        if best == len(nums) + 1:
            return 0
        return best
