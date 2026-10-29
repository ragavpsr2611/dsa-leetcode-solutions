"""
LeetCode 88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

Pattern: two pointers (two arrays), merging from the back

Time:  O(m + n)  - k starts at m + n - 1 and moves one slot left every
                   iteration, so there are at most m + n iterations
Space: O(1)      - merged in place; only three index variables
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
