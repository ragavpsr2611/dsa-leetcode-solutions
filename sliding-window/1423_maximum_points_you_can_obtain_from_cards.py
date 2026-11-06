"""
LeetCode 1423. Maximum Points You Can Obtain from Cards
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

Pattern: sliding split between the two ends: start with all k cards from the
         left, then swap them one at a time for cards from the right end

Time:  O(k)  - one loop to sum the first k cards, one loop of k swaps
Space: O(1)  - a few integers only
"""


class Solution(object):
    def maxScore(self, cardPoints, k):
        a = 0
        for i in range(k):
            a += cardPoints[i]
        d = a
        c = k - 1
        for i in range(len(cardPoints) - 1, len(cardPoints) - 1 - k, -1):
            a += cardPoints[i] - cardPoints[c]
            c -= 1
            d = max(a, d)

        return d
