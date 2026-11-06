"""
LeetCode 27. Remove Element
https://leetcode.com/problems/remove-element/

Pattern: two pointers (same direction, read/write)

Time:  O(n)  - a single pass; the read pointer visits each element once
Space: O(1)  - done in place; only two integer variables are created
"""


class Solution(object):
    def removeElement(self, nums, val):
        w = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[w] = nums[i]
                w += 1
        return w
