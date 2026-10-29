"""
LeetCode 11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Pattern: two pointers (opposite ends)

Time:  O(n)  - each iteration moves one pointer inward and neither moves back,
               so the loop runs n - 1 times
Space: O(1)  - only a few variables
"""


class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        max = 0
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            a = w * h
            if a > max:
                max = a
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max
