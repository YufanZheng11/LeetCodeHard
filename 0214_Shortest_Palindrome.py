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

import cProfile


class Solution:

    def shortestPalindrome(self, s):
        n = len(s)
        if n <= 1:
            return s
        shortest = None
        for i in range(n//2):
            shortest = self.updateShortest(s, i, i, shortest, n)
            if s[i] == s[i+1]:
                shortest = self.updateShortest(s, i, i+1, shortest, n)
        if n % 2 == 1:
            shortest = self.updateShortest(s, n//2, n//2, shortest, n)
        return shortest

    def updateShortest(self, s, left, right, shortest, n):
        left, right = self.expandAtCenter(s, left, right, n)
        if left == 0:
            current = self.formPalindrome(s, right)
            if not shortest or len(shortest) > len(current):
                shortest = current
        return shortest

    def expandAtCenter(self, s, left, right, n):
        while left >= 1 and right < n-1 and s[left-1] == s[right+1]:
            left -= 1
            right += 1
        return left, right

    def formPalindrome(self, s, right):
        return s[right+1:][::-1] + s


if __name__ == '__main__':
    s = Solution()
    string = "a" * 5000
    cProfile.run("s.shortestPalindrome(string)")