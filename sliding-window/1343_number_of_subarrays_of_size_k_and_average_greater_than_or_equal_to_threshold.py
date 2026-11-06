"""
LeetCode 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

Pattern: sliding window (fixed size)

Time:  O(n)  - the first window costs k, then each of the n - k slides is
               one addition and one subtraction: k + (n - k) = n
Space: O(1)  - the first window is summed with a loop, so no slice is copied;
               the check compares sums (a >= threshold * k), so no division
"""


class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        c = 0
        a = 0
        for i in range(k):
            a += arr[i]
        if a >= threshold * k:
            c += 1

        for i in range(k, len(arr)):
            a += arr[i] - arr[i - k]
            if a >= threshold * k:
                c += 1
        return c
