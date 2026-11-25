class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        a=[[1]*(i+1) for i in range(numRows)]
        if numRows>2:
            for i in range(2,numRows):
                for j in range(1,i):
                    #if j!=0 and j!=2:
                        a[i][j]=a[i-1][j]+a[i-1][j-1]
        return a
