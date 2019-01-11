/*
Question:

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

'''
In this question, we can already find how dp table looks like,which is the same as the given matrix.
In terms of how we should fill in this table, we can find that, the base case is the first row and the 
first column, they have no chance to form a bigger square, therefore we keep these value in the dp table,
dp table should look like this when just fill in the base case:
1 0 1 0 0
1 x x x x
1 x x x x
1 x x x x
To the other cell. if the number is 0, then it has no chance to form a square, so we fill 0 in the dp table.
If the number is 1, then we should check upper, left and diagonal number, if all of them are not zero, then 
there must be a squre. So the rule is table[i][j]=min(table[i-1][j],table[i][j-1],table[i-i][j-1])+1
*/
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int res=0;
        if(matrix.size()==0)
            return res;
        int m=matrix.size(),n=matrix[0].size();
        vector<vector<int>> table(m,vector<int>(n));

        for(int i=0;i<m;++i){
            table[i][0]=matrix[i][0]-'0';
            res=max(res,table[i][0]);
        }
        for(int j=0;j<n;++j){
            table[0][j]=matrix[0][j]-'0';
            res=max(res,table[0][j]);
        }
        for(int i=1;i<m;++i){
            for(int j=1;j<n;++j){
                if(matrix[i][j]=='0')
                    continue;
                table[i][j]=min(table[i][j-1],min(table[i-1][j],table[i-1][j-1]))+1;
            res=max(res,table[i][j]);
            }
                   
        }
        /*for(int i=0;i<m;i++){
            for(int j=0;j<n;j++)
                cout<<table[i][j]<<" "; 
            cout<<endl;
        }*/
        
        return pow(res,2);
    }
};
