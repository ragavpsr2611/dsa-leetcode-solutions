"""
LeetCode 75. Sort Colors
https://leetcode.com/problems/sort-colors/

Pattern: three pointers (Dutch national flag), partition in place in one pass
         [0 .. l-1] zeros | [l .. m-1] ones | [m .. h] unseen | [h+1 ..] twos

Time:  O(n)  - one pass; each step moves m forward or h backward, and they
               meet after at most n steps in total
Space: O(1)  - swaps happen inside the input; only three indexes are created
"""


class Solution(object):
    def sortColors(self, nums):
        l, m, h = 0, 0, len(nums) - 1
        while m <= h:
            if nums[m] == 2:
                nums[m], nums[h] = nums[h], nums[m]
                h -= 1
            elif nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            else:
                m += 1

        return nums
