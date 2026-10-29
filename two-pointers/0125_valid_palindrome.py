"""
LeetCode 125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Pattern: two pointers (opposite ends)

Approach: Keep one pointer at each end. If the left character is not
alphanumeric, move the left pointer right; if the right character is not
alphanumeric, move the right pointer left. When both are alphanumeric, compare
them: if they match, move both pointers inward, otherwise return False.

Time:  O(n)  - each iteration moves at least one pointer inward
Space: O(n)  - s.lower() makes a copy of the string. Lowercasing each character
               at the comparison instead would make this O(1).
"""


class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            elif s[l].isalnum() == False:
                l += 1
            else:
                r -= 1
        return True
