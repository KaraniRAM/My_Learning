class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #f=False
        ro=len(matrix)
        co=len(matrix[0])
        l=0
        r=(co*ro)-1
        while l<=r:
            mid=(l+r)//2
            rr=mid//co
            cc=mid%co
            if matrix[rr][cc]==target:
                #f=True
                #break
                return True
            elif matrix[rr][cc]<target:
                l=mid+1
            else:
                r=mid-1
        
        #return f
        return False