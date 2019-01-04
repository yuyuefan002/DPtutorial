"""
Question:
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
"""
Solution:

According to the question, we already know what dp table looks
like and how can we fill in dp table. Note that since path only go
either down or right, which means each cell only depends on its upper
and left, therefore, we can fill in the table row by row or column by column.

To each cell, we pick the smaller sum between upper and left, 
finally we can get the result at the bottom right.
Note that the result is at the bottom right is because 
this cell presents the size of the problem.
In other words, every cell is the answer to its size.
if cell[i][j]=5, then given a i*j grid filled with non-negative numbers,
we can find a min sum which is 5. 
"""

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        res=[[0 for i in range(n)]for j in range(m)]
        
        # base case, [0][0]should be itself
        res[0][0]=grid[0][0]
        
        # base case, column=0, the first row only depends on the previous row
        for i in range(1,m):
            res[i][0]=res[i-1][0]+grid[i][0]
        
        # base case, row=0, the first column only depends on the previous column
        for j in range(1,n):
            res[0][j]=res[0][j-1]+grid[0][j]
        
        for i in range(1,m):
            for j in range(1,n):
                # pick the smaller between upper and left
                res[i][j]=min(res[i-1][j],res[i][j-1])+grid[i][j]
        
        return res[-1][-1]
