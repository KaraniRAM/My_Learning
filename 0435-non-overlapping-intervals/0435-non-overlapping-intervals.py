class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[1])
        e=intervals[0][1]
        c=len(intervals)
        i=1
        while i <(len(intervals)):
            if intervals[i][0]<e:
                intervals.pop(i)
            else:
                e=intervals[i][1]
                i+=1
        return c-len(intervals)