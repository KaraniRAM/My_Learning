class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix=[[0]*n for i in range(n)]
        num=1
        i=j=0
        nn=0
        r=n-1
        
        while nn<=r:
            while j<=r:
                (matrix[i][j])=num
                num+=1
                j+=1
            j-=1
            i+=1
            while i<=r:
                (matrix[i][j])=num
                num+=1
                i+=1
            i-=1
            j-=1
            while j>=nn and nn<r:
                (matrix[i][j])=num
                num+=1
                j-=1
            j+=1
            i-=1
            while i>nn and nn<r:
                (matrix[i][j])=num
                num+=1
                i-=1
            i+=1
            nn+=1
            r-=1
            j+=1
        return matrix
        