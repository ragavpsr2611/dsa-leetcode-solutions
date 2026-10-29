"""
LeetCode 26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Pattern: two pointers (same direction, read/write)

Time:  O(n)  - a single pass; the read pointer visits each element once
Space: O(1)  - done in place with one extra index
"""


class Solution(object):
    def removeDuplicates(self, nums):
        w = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[w - 1]:
                nums[w] = nums[i]
                w += 1
        return w
