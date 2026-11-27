class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tot=0
        curr=0
        st_station=0
        for i in range(len(gas)):
            diff=gas[i]-cost[i]
            tot+=diff
            curr+=diff
            if curr<0:
                st_station=i+1
                curr=0
        if tot<0:
            return -1
        return st_station
        