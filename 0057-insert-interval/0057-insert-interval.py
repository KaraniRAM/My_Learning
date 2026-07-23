class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()
        e=intervals[0][1]
        r=[]
        g=[]
        r.append(intervals[0][0])
        #return intervals
        for i in range(1,len(intervals)):
            if intervals[i][0]<=e:
                e=max(e,intervals[i][1])
            else:
                r.append(e)
                g.append(r)
                r=[]
                r.append(intervals[i][0])
                e=intervals[i][1]
        r.append(e)
        g.append(r)
        return g
        