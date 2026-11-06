"""
LeetCode 1768. Merge Strings Alternately
https://leetcode.com/problems/merge-strings-alternately/

Pattern: two sequences, one index; the leftover tail is appended at the end

Time:  O(m + n)  - the loop runs min(m, n) times, then the tail and the join
                   each touch every remaining character once
Space: O(m + n)  - the list holds about one entry per output character
                   (the output is the whole answer here)
"""


class Solution(object):
    def mergeAlternately(self, word1, word2):
        c = min(len(word1), len(word2))
        d = []
        for i in range(c):
            d.append(word1[i])
            d.append(word2[i])
        d.append(word2[c:])
        d.append(word1[c:])

        return "".join(d)
