"""
LeetCode 392. Is Subsequence
https://leetcode.com/problems/is-subsequence/

Pattern: two pointers (two sequences)

Time:  O(len(t))  - j moves forward one step every iteration and never goes
                    back, so the loop runs at most len(t) times
Space: O(1)       - only a few index variables
"""


class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        j = 0
        k = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
                k += 1
            else:
                j += 1
        if k == len(s):
            return True
        else:
            return False
