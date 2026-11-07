"""
LeetCode 1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/

Pattern: sliding window (variable size), longest window with at most k zeros
         (flipping at most k zeros = allowing at most k zeros in the window)

Time:  O(n)  - i moves right n times; l only moves right, at most n times
               in total
Space: O(1)  - a few integers
"""


class Solution(object):
    def longestOnes(self, nums, k):
        best = 0
        l = 0
        c = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                c += 1
            while c > k:
                if nums[l] == 0:
                    c -= 1
                l += 1
            best = max(best, i - l + 1)

        return best
