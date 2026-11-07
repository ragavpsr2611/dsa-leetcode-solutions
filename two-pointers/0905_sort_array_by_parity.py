"""
LeetCode 905. Sort Array By Parity
https://leetcode.com/problems/sort-array-by-parity/

Pattern: two pointers (same direction, read/write)

Time:  O(n)  - one pass over the array
Space: O(1)  - sorted in place, only a few index variables
"""


class Solution(object):
    def sortArrayByParity(self, nums):
        l = 0
        w = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[w], nums[l] = nums[l], nums[w]
                l += 1
                w += 1
            else:
                l += 1
        return nums
