"""
LeetCode 167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Pattern: two pointers (opposite ends)

Approach: (write this in your own words)

Time:  O(n)  - each step moves one pointer inward; they never move back
Space: O(1)
"""


class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]  # the problem uses 1-based indices
            elif s < target:
                l += 1
            else:
                r -= 1
