class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        i=0
        j=0
        g=[]
    
        while i<len(firstList) and j <len(secondList):
            l=max(firstList[i][0],secondList[j][0])
            r=min(firstList[i][1],secondList[j][1])
            if l<=r:
                g.append([l,r])
            
            if firstList[i][1]<secondList[j][1]:
               
                i+=1
            else:
                j+=1
        return g

