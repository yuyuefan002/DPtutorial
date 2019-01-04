"""
Question:

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

"""
Solution:

According to the question, we can obtain what dp table
looks like and how we can fill in dp table. The dp table 
is also a triangle.
We have two way to fill in the table, from top to bottom and
from bottom to top, latter one is better. It is easier to index
and no special case. Note that we have to pick the min among the last 
row if we use top to bottom method.

Each cell is just related to its two children, we just need to pick the
smaller one between them.
"""
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # iterate from bottom to top
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                
                # pick the smaller one between two children
                sum = min(triangle[i+1][j],triangle[i+1][j+1])
                triangle[i][j] = sum + triangle[i][j]
        
        return triangle[0][0]
