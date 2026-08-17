class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        k=bin(n)[2:].zfill(32)
        g=k[::-1]
        h=int(g,2)
        return h
        