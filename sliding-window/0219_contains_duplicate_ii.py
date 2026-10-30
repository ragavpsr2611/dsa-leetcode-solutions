"""
LeetCode 219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/

Pattern: sliding window (fixed size), with a set holding the window's values

Time:  O(n)          - one pass; set membership, add and remove are O(1)
                       on average
Space: O(min(n, k))  - the set never holds more than k values after each
                       step (a value is removed whenever it grows past k)
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        a = set()
        for i in range(len(nums)):
            if nums[i] in a:
                return True
            a.add(nums[i])
            if len(a) > k:
                a.remove(nums[i - k])
        return False
