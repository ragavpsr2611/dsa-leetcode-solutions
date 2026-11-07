"""
LeetCode 3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Pattern: sliding window (variable size, set), longest window with no repeat

Time:  O(n)           - i moves right n times; l only moves right, at most n
                        times in total; set add/remove/lookup are O(1) on
                        average
Space: O(min(n, m))   - the set holds distinct characters only, so it is
                        bounded by n and by the alphabet size m
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        a = set()
        l = 0
        best = 0
        for i in range(len(s)):
            while s[i] in a:
                a.remove(s[l])
                l += 1
            a.add(s[i])
            best = max(best, i - l + 1)

        return best
