class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x:x[1])
        c=0
        e=float('-inf')
        for i in range(len(points)):
            if points[i][0]>e:
                c+=1
                e=points[i][1]
        return c