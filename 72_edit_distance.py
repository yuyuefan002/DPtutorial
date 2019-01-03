'''
At the first step, we should use a more straight forward
way to solve the problem, recursion is recommended. This
method is called use-it-or-lose-it. The idea is aligned 
with the way you read the problem.
'''
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # base case: one string emtpy
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1),len(word2))
        
        # base case: if two letter same
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:],word2[1:])
        
        # insert into word1
        A = self.minDistance(word1,word2[1:])
        
        # delete in word1
        B = self.minDistance(word1[1:],word2)

        # replace in word1
        C = self.minDistance(word1[1:],word2[1:])
        
        return min(A,B,C)+1

'''
At the second step, we should convert this recursive
solution into DP table, with the DP table, we can generate
the DP solution
e.g.
word1 = "horse", word2 = "ros"
    s o r
  _ _ _ _
 |0 1 2 3
e|1 1 2 3
s|2 1 2 3
r|3 2 2 2
o|4 3 2 3
h|5 4 3 3

How could we fill in this table?
1. According to our recursive method, we start from the end of each string, 
   therefore, we write it in the reverse way
2. Fill in the base case, which is the first row and the first column
3. Fill in the rest of the table row by row or column by column, the rule
   is:
   a) if two letters equal, pick the diagonal number
   b) if two letters differ, pick the min among upper, left and diagonal plus one
note that since the current number only related to the number left and above, so 
we can fill the table row by row/column by column
'''

'''
At the third step, we write the DP solution using the way we fill in the table
'''
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1,l2=len(word1)+1,len(word2)+1
        
        # generate the empty table
        table=[[0 for i in range(l2)]for j in range(l1)]
        
        # fill in the base case
        for i in range(l1):
            table[i][0]=i
        for j in range(l2):
            table[0][j]=j
        
        # fill in the table row by row
        for i in range(1,l1):
            for j in range(1,l2):
                
                # if two letters equal, pick diagonal
                if word1[i-1] == word2[j-1]:
                    table[i][j]=table[i-1][j-1]
                
                # if two letters differ, pick the min among upper,left and diagonal
                else:
                    table[i][j]=min(table[i][j-1],table[i-1][j],table[i-1][j-1])+1
        
        # return the bottom right cell
        return table[-1][-1]
