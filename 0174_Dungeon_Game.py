"""

https://leetcode.com/problems/dungeon-game/

The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon.
The dungeon consists of m x n rooms laid out in a 2D grid.
Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms;
other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.


Example 1:

Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.

Example 2:

Input: dungeon = [[0]]
Output: 1
"""


class Solution:

    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        cache = [[0] * n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1:
                    if j == n-1:
                        cache[i][j] = max(1, 1-dungeon[i][j])
                    else:
                        cache[i][j] = max(1, cache[i][j+1]-dungeon[i][j])
                else:
                    if j == n-1:
                        cache[i][j] = max(1, cache[i+1][j]-dungeon[i][j])
                    else:
                        way1 = max(1, cache[i+1][j]-dungeon[i][j])
                        way2 = max(1, cache[i][j+1]-dungeon[i][j])
                        cache[i][j] = min(way1, way2)
        return cache[0][0]
