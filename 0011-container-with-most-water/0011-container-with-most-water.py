class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        
        maxi=0
        while i<j:
            l=min(height[i],height[j])
            b=j-i
            maxi=max(maxi,l*b)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxi
        