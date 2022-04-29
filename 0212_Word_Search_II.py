"""
https://leetcode.com/problems/word-search-ii/

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once in a word.


Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""


class Solution:

    def findWords(self, board, words):
        trie = self.buildTrie(words)
        m, n = len(board), len(board[0])
        matched = []
        for i in range(m):
            for j in range(n):
                for word in self.bfs(board, i, j, m, n, trie):
                    matched.append(word)
        return list(set(matched))

    def bfs(self, board, i, j, m, n, trie):
        queue = [[(i, j), [(i, j)], trie]]
        matched = []
        while queue:
            (i, j), path, p = queue.pop()
            ch = board[i][j]
            if ch in p:
                if 'end' in p[ch]:
                    word = ''.join(board[u][v] for u, v in path)
                    matched.append(word)
                for u, v in self.neighbors(i, j, m, n):
                    if (u, v) not in path:
                        queue.append([(u, v), path + [(u, v)], p[ch]])
        return matched

    def neighbors(self, i, j, m, n):
        for u, v in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= u < m and 0 <= v < n:
                yield u, v

    def buildTrie(self, words):
        trie = {}
        for word in words:
            p = trie
            for ch in word:
                if ch not in p:
                    p[ch] = {}
                p = p[ch]
            p['end'] = ''
        return trie


if __name__ == '__main__':
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    s = Solution()
    print(s.findWords(board, words))
