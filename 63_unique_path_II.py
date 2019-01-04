"""
Question:

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2

Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

"""
Solution:

In the last question, we solve the problem using three steps:
1.writing recursive solution, 2.drawing dp table, 3.writing dp
solution
However, in this case, we don't need to do so. After observing the 
question, I found the question itself already tells us 
what dp table looks like and how can we fill in this table,
if both left and upper are obstacles,then no path, 
if only left is an obstacle, pick upper number,
if only upper is an obstacle, pick left number,
else, add both numbers
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        res=[[0 for i in range(n+1)]for j in range(m+1)]
        res[0][1]=1
        for i in range(m):
            for j in range(n):
                # lose it, if it is a obstacle skip
                if obstacleGrid[i][j] == 1:
                    continue
                # use it, if it is a path
                res[i+1][j+1]=res[i][j+1]+res[i+1][j]

        return res[-1][-1]
