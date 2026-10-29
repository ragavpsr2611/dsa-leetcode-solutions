"""
LeetCode 977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/

Pattern: two pointers (opposite ends), filling the result from the back

Time:  O(n)  - each iteration places one square and moves one pointer inward,
               so the loop runs exactly n times
Space: O(1)  - extra space; the result array is the output, which is not
               counted (O(n) if you count it)
"""


class Solution(object):
    def sortedSquares(self, nums):
        l = 0
        r = len(nums) - 1
        dup = [0] * len(nums)
        pos = len(nums) - 1
        while l <= r:
            left = nums[l] ** 2
            right = nums[r] ** 2
            if left > right:
                dup[pos] = left
                l += 1
            else:
                dup[pos] = right
                r -= 1
            pos -= 1
        return dup
