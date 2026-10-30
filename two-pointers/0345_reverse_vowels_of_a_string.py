"""
LeetCode 345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/

Pattern: two pointers (opposite ends), skipping non-vowels

Time:  O(n)  - each iteration moves at least one pointer inward
Space: O(n)  - Python strings are immutable, so the string is copied into a
               list to allow swapping (O(1) in a language with mutable strings)
"""


class Solution(object):
    def reverseVowels(self, s):
        l = 0
        r = len(s) - 1
        a = "aeiouAEIOU"
        b = list(s)
        while l < r:
            if b[l] in a and b[r] in a:
                b[l], b[r] = b[r], b[l]
                l += 1
                r -= 1
            elif b[l] not in a:
                l += 1
            elif b[r] not in a:
                r -= 1
        s = "".join(b)
        return s
