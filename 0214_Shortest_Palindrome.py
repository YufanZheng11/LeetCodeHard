"""
https://leetcode.com/problems/shortest-palindrome/

You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.


Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"

Example 2:

Input: s = "abcd"
Output: "dcbabcd"

Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
"""


class Solution:

    def shortestPalindrome(self, s):
        n = len(s)
        if n <= 1:
            return s
        for right in range(n-1, -1, -1):
            if self.isPalindrome(s, 0, right):
                return s[right+1:][::-1] + s

    def isPalindrome(self, s, left, right):
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    string = "aacecaaa"
    s.shortestPalindrome(string)