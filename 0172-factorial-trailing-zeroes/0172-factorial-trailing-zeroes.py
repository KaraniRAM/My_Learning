class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        z=0
        while n>0:
            n//=5
            z+=n
        return z
        