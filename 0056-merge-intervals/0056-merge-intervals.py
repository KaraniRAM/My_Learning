class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        r=[]
        r.append(intervals[0][0])
        g=[]
        e=intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=e:
                e=max(e,intervals[i][1])
            else:
                r.append(e)
                g.append(r)
                r=[]
                r.append(intervals[i][0])
                e=max(e,intervals[i][1])
        r.append(e)
        g.append(r)
        return g
