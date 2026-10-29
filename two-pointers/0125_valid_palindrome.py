"""
LeetCode 125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Pattern: two pointers (opposite ends)

Approach: Keep one pointer at each end. If the left character is not
alphanumeric, move the left pointer right; if the right character is not
alphanumeric, move the right pointer left. When both are alphanumeric, compare
them: if they match, move both pointers inward, otherwise return False.

Time:  O(n)  
Space: O(1)  
"""


class Solution(object):
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
            elif s[l].isalnum() == False:
                l += 1
            else:
                r -= 1
        return True
