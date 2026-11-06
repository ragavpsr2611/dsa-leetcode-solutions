"""
LeetCode 680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/

Pattern: two pointers (opposite ends); at the first mismatch try BOTH deletions

Time:  O(n)  - the main loop stops at the first mismatch, then at most two
               index-based palindrome checks of up to n characters each
Space: O(1)  - the helper takes indexes instead of slicing, so nothing is copied
"""


class Solution(object):
    def validPalindrome(self, s):
        def is_pal(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_pal(l, r - 1) or is_pal(l + 1, r)
            l += 1
            r -= 1
        return True
