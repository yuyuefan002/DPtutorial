'''
Question:

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
'''


'''
step 1, come up with a recursive solution. To me, I come up with
a recursive solution at first easily. In this solution, we take 
every situation into consideration, to each num, we consider it as
a negative number or positive number substracted to the current sum. When
we reach the end of the array, we check whether the sum is zero.
'''

class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # base case:reach the end
        if len(nums)==0:
            if S==0:
                return 1
            else:
                return 0
        # use it: take next number as pos
        A=self.findTargetSumWays(nums[1:],S-nums[0])
        
        # lose it: take next number as neg
        B=self.findTargetSumWays(nums[1:],S+nums[0])
        
        return A+B
'''
step 2, draw the dp table, and determin how to fill in this table.
In this question, dp table looks like a tree, if we draw table for 
the example, it looks like:
                0
             1 / \ -1
              1  -1
             / \ / \
            2  0 0  -2
               ...
We can fill it from top to bottom, row by row. 
Note that there are some repeated value during each level, and it 
is not necessary to store the whole tree, so we use hashmap to store
the number frequency in each level
'''


'''
step 3, we should translate the process of how we fill in the table 
into code.
'''
class Solution(object):
    def findTargetSumWays(self, nums, S):
        # base case: no num
        if len(nums)==0:
            return 0

        # generate the first level
        res = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}

        # fill in the table level by level, store in the map
        for i in range(1, len(nums)):
            new = {}
            for n in res:
                new[n + nums[i]] = new.get(n + nums[i], 0) + res.get(n, 0)
                new[n - nums[i]] = new.get(n - nums[i], 0) + res.get(n, 0)

            # only store one level
            res = new

        # get the frequency
        return res.get(S, 0)
    
