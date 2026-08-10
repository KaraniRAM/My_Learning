class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        s=0
        for i in range(len(mat)):
            for j in range(len(mat)):   
                if j==i:
                    s+=mat[i][j]
        #return s
        i=0;j=len(mat)-1
        while i<len(mat):
            if i!=j:
                s+=mat[i][j]
            j-=1
            i+=1
        return s
        