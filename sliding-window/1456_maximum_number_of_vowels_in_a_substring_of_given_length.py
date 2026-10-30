"""
LeetCode 1456. Maximum Number of Vowels in a Substring of Given Length
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

Pattern: sliding window (fixed size)

Time:  O(n)  - the first window costs k, then each of the remaining n - k
               slides is constant work: k + (n - k) = n
Space: O(1)  - a few variables; no slices are made
"""


class Solution(object):
    def maxVowels(self, s, k):
        a = "aeiou"
        best = 0
        for i in range(k):
            if s[i] in a:
                best += 1
        cur = best
        for i in range(k, len(s)):
            if s[i] in a:
                cur += 1
            if s[i - k] in a:
                cur -= 1
            best = max(cur, best)
        return best
