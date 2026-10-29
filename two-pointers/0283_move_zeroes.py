"""
LeetCode 283. Move Zeroes
https://leetcode.com/problems/move-zeroes/

Pattern: two pointers (same direction, read/write)

Time:  O(n)  - two loops one after the other, so the costs add:
               n + (n - w) <= 2n
Space: O(1)  - done in place
"""


class Solution(object):
    def moveZeroes(self, nums):
        l = 0
        w = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                pass
            else:
                nums[w] = nums[i]
                w += 1
        for i in range(w, len(nums)):
            nums[i] = 0
        return nums
